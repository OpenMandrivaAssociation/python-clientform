%define oname ClientForm

Summary:	Client-side HTML form handling
Name:		python2-clientform
Version:	0.2.10
Release:	13
License:	BSD
Group:		Development/Python
Url:		http://wwwsearch.sourceforge.net/ClientForm/
Source0:	http://wwwsearch.sourceforge.net/%{oname}/src/%{oname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python2-setuptools
BuildRequires:  python-setuptools
BuildRequires:	pkgconfig(python2)
%rename python-%oname

%description
ClientForm is a Python module for handling HTML forms on the client
side, useful for parsing HTML forms, filling them in and returning the
completed forms to the server.  It developed from a port of Gisle Aas'
Perl module HTML::Form, from the libwww-perl library, but the
interface is not the same.

%prep
%setup -qn %{oname}-%{version}

%build
python2 setup.py build

%install
python2 setup.py install --single-version-externally-managed --root=%{buildroot}

%files
%doc *txt *html
%{py2_puresitedir}/%{oname}*

