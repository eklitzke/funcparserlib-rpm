# Created by pyp2rpm-3.3.2
%global pypi_name funcparserlib

Name:           python-%{pypi_name}
Version:        0.3.6
Release:        1%{?dist}
Summary:        Recursive descent parsing library based on functional combinators

License:        MIT
URL:            http://code.google.com/p/funcparserlib/
Source0:        https://files.pythonhosted.org/packages/source/f/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Description
-----------

*Parser combinators* are just higher-order functions
that take parsers as their
arguments and return them as result values. Parser
combinators are:

* First-class values
* Extremely composable
* Tend to make
the code quite compact
* Resemble the readable notation of xBNF grammars
Parsers made with ``funcparserlib`` are pure-Python LL(*) parsers. It means
that it's...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Description
-----------

*Parser combinators* are just higher-order functions
that take parsers as their
arguments and return them as result values. Parser
combinators are:

* First-class values
* Extremely composable
* Tend to make
the code quite compact
* Resemble the readable notation of xBNF grammars
Parsers made with ``funcparserlib`` are pure-Python LL(*) parsers. It means
that it's...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python2} -m unittest discover funcparserlib.tests

%files -n python3-%{pypi_name}
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Mar 26 2019 mockbuilder - 0.3.6-1
- Initial package.
