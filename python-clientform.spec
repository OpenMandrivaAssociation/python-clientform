%define oname ClientForm

Summary:	Client-side HTML form handling
Name:		python-clientform
Version:	0.2.10
Release:	%{mkrel 1}
Source0:	http://wwwsearch.sourceforge.net/%{oname}/src/%{oname}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
URL:		http://wwwsearch.sourceforge.net/ClientForm/
BuildRequires:	python-devel
BuildRequires:	python-setuptools

%description
ClientForm is a Python module for handling HTML forms on the client
side, useful for parsing HTML forms, filling them in and returning the
completed forms to the server.  It developed from a port of Gisle Aas'
Perl module HTML::Form, from the libwww-perl library, but the
interface is not the same.

%prep
%setup -q -n %{oname}-%{version}

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --single-version-externally-managed --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc *txt *html
%{py_platsitedir}/%{oname}*

