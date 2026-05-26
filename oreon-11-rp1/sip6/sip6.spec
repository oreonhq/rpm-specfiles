# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 83f5619b87788a134e151560b954ab312e44a9763d935c0e419bbe5b8aa79b11
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%global pypi_name sip

Name:           sip6
Version:        6.15.1
Release:        1%{?dist}
Summary:        SIP - Python/C++ Bindings Generator
%py_provides    python3-sip6

License:        BSD-2-Clause
URL:            https://github.com/Python-SIP/sip
Source0:        https://github.com/Python-SIP/sip/archive/6.15.1/sip-6.15.1.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

# For tests
BuildRequires:  gcc-c++

%global _description %{expand:
SIP is a collection of tools that makes it very easy to create Python bindings
for C and C++ libraries.  It was originally developed in 1998 to create PyQt,
the Python bindings for the Qt toolkit, but can be used to create bindings for
any C or C++ library.  For example it is also used to generate wxPython, the
Python bindings for wxWidgets.}

%description %_description

%prep
%oreon_verify_sources
%autosetup -n %{pypi_name}-%{version} -p 1

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install

#check
#{py3_test_envvars} {python3} -m unittest discover -v -s test


%files
%doc README.md
%license LICENSE
%{_bindir}/sip*
%{python3_sitelib}/sip-*
%{python3_sitelib}/sipbuild/

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.15.1-1
- Prepare for Oreon 11 (RP1)
