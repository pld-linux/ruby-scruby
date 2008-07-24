Summary:	A portable, customizable packet creation
Name:		ruby-scruby
Version:	0.3
Release:	0.1
License:	GPL v2
Group:		Development/Libraries
Source0:	http://sylv1.tuxfamily.org/projects/scruby/scruby-%{version}.tar.gz
# Source0-md5:	c049dc42eb1f92c31dd2e37c3997fa29
URL:		http://sylv1.tuxfamily.org/projects/scruby.html
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
BuildRequires:	setup.rb
#BuildArch:	noarch
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# not noarch only due ruby packaging
%define		_enable_debug_packages	0

%description
Scruby is a portable, customizable packet creation and
sending/sniffing tool written in Ruby. It was tested on NetBSD,
GNU/Linux and MacOS X, and should theoretically work on some other
platforms such as FreeBSD, OpenBSD, and proprietary Unixes.

%prep
%setup -q -n scruby-%{version}

%build
cp %{_datadir}/setup.rb .
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc -o rdoc scruby

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_rubylibdir}
ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc CHANGELOG
