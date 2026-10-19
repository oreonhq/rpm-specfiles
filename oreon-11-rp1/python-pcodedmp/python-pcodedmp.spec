%global source0_hash 41ef07101c5807a5dfe7c36caa28678457630e4a8a092792acf2eb473f1b9e67
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
Name:           python-pcodedmp
Summary:        VBA p-code disassembler
Version:        1.2.6
Release:        1%{?dist}
License:        GPL-3.0-or-later
URL:            https://github.com/bontchev/pcodedmp
VCS:            https://github.com/bontchev/pcodedmp
BuildArch:      noarch
%global srcname pcodedmp
%bcond_with     bootstrap
%bcond_with     pypandoc
Source0:        https://files.pythonhosted.org/packages/source/p/python-pcodedmp/python-pcodedmp-%{version}.tar.gz
# oreon:deps
BuildRequires:  python3-devel
# /oreon:deps
%description

%package -n pcodedmp
Summary:        VBA p-code disassembler
Requires:       python3-pcodedmp = %{version}-%{release}
%description -n pcodedmp

%package -n python3-pcodedmp
Summary:        VBA p-code disassembler
BuildRequires:  python3-devel
%if %{with pypandoc}
BuildRequires:  python3-pypandoc
%endif
%if %{without bootstrap}
BuildRequires:  python3-lxml
BuildRequires:  python3-oletools >= 0.54
Requires:       python3-oletools >= 0.54
%endif
%description -n python3-pcodedmp

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pcodedmp-%{version}
%oreon_prep
%build

%py3_build
%install
%py3_install
%oreon_autofiles pcodedmp usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-pcodedmp usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{without bootstrap}
%check

%py3_check_import pcodedmp
%endif
%files -f %{oreon_filedir}/main.list
%files -n pcodedmp -f %{oreon_filedir}/pcodedmp.list
%files -n python3-pcodedmp -f %{oreon_filedir}/python3-pcodedmp.list

%changelog

%autochangelog
