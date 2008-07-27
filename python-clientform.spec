%define oname ClientForm
%define version 0.2.9
%define unmangled_version 0.2.9
%define unmangled_version 0.2.9
%define release %mkrel 1

Summary: Client-side HTML form handling
Name: python-clientform
Version: %{version}
Release: %{release}
Source0: %{oname}-%{unmangled_version}.tar.gz
License: BSD
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Url: http://wwwsearch.sourceforge.net/ClientForm/
BuildRequires: python-devel

%description
ClientForm is a Python module for handling HTML forms on the client
side, useful for parsing HTML forms, filling them in and returning the
completed forms to the server.  It developed from a port of Gisle Aas'
Perl module HTML::Form, from the libwww-perl library, but the
interface is not the same.


%prep
%setup -q -n %{oname}-%{unmangled_version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --single-version-externally-managed --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc *txt *html
%py_platsitedir/%{oname}*
