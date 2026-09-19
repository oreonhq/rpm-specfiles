%global source0_hash 9444278d47161d5f2be76a767809a3cbe6db4db822f46a4fd7481d4057208d41

%global		oname Parsley
%global		lowname parsley

Name:		python-parsley
Version:	1.3
Release:	38%{?dist}
Summary:	Parsing and pattern matching made easy
License:	MIT
URL:		https://launchpad.net/parsley
Source0:	https://files.pythonhosted.org/packages/source/P/%{oname}/%{oname}-%{version}.tar.gz
Patch:		tests-replace-usage-of-obsolete-TestCase-methods.patch
BuildArch:	noarch

BuildRequires: make
BuildRequires:	python3-devel
BuildRequires:	python3-pytest
BuildRequires:	python3-twisted
BuildRequires:	python3-sphinx

%global _description\
A parser generator library based on OMeta, and other useful parsing tools.\
Parsley is a parsing library for people who find parsers scary or\
annoying. I wrote it because I wanted to parse a programming language,\
and tools like PLY or ANTLR or Bison were very hard to understand and\
integrate into my Python code. Most parser generators are based on LL\
or LR parsing algorithms that compile to big state machine\
tables. It was like I had to wake up a different section of my brain\
to understand or work on grammar rules.\
\
Parsley, like pyparsing and ZestyParser, uses the PEG algorithm, so\
each expression in the grammar rules works like a Python\
expression. In particular, alternatives are evaluated in order, unlike\
table-driven parsers such as yacc, bison or PLY.\
\
Parsley is an implementation of OMeta, an object-oriented\
pattern-matching language developed by Alessandro Warth at\
thesis, which provides a detailed description of OMeta:\
http://www.vpri.org/pdf/tr2008003_experimenting.pdf

%description %_description

%package -n python3-parsley
Summary: %summary
%{?python_provide:%python_provide python3-parsley}

%description -n python3-parsley %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{oname}-%{version}
rm -rf *.egg*

%build
%py3_build
make -C doc html man
rm -f doc/_build/html/.buildinfo

%install
%py3_install
mkdir -p %{buildroot}%{_mandir}/man1
cp -a %{_builddir}/%{oname}-%{version}/doc/_build/man/%{lowname}.1* %{buildroot}%{_mandir}/man1

%check
# Exclude only test_vm_builder tests, as they are failing due to missing vm files.
py.test-%{python3_version} terml/test ometa/test --ignore=ometa/test/test_vm_builder.py

%files -n python3-parsley
%license LICENSE
%doc NEWS README
%{_mandir}/man1/%{lowname}.1*
%{python3_sitelib}/%{oname}-%{version}-py3.*.egg-info
%{python3_sitelib}/ometa/
%{python3_sitelib}/__pycache__/%{lowname}.*
%{python3_sitelib}/%{lowname}.*
%{python3_sitelib}/terml/

%changelog
%autochangelog
