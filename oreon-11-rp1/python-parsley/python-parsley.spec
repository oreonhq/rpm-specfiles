%global source0_hash 9444278d47161d5f2be76a767809a3cbe6db4db822f46a4fd7481d4057208d41
%global		oname Parsley
%global		lowname parsley
Name:		python-parsley
Version:	1.3
Release:        1%{?dist}
Summary:        Parsing and pattern matching made easy
License:	MIT
URL:		https://launchpad.net/parsley
Source0:        https://files.pythonhosted.org/packages/source/P/%{oname}/%{oname}-%{version}.tar.gz
Patch:		tests-replace-usage-of-obsolete-TestCase-methods.patch
BuildArch:	noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-sphinx
BuildRequires:  python3-twisted
# /oreon:deps
%description

%package -n python3-parsley
Summary: %summary
%{?python_provide:%python_provide python3-parsley}
%description -n python3-parsley

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
%oreon_autofiles python3-parsley usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

py.test-%{python3_version} terml/test ometa/test --ignore=ometa/test/test_vm_builder.py
%files -f %{oreon_filedir}/main.list
%files -n python3-parsley -f %{oreon_filedir}/python3-parsley.list

%changelog

%autochangelog
