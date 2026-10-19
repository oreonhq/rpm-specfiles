%global source0_hash f8d69dfbc6ccb582896d40a9a69457aa1075cdd6efbc55d34c797024b40bcc38
Name:           python-mailman-hyperkitty
Version:        1.2.1
Release:        1%{?dist}
Summary:        Mailman archiver plugin for HyperKitty
License:        GPL-3.0-or-later
URL:            https://gitlab.com/mailman/mailman-hyperkitty/
Source0:        https://files.pythonhosted.org/packages/source/m/mailman-hyperkitty/mailman-hyperkitty-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-mailman-hyperkitty = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-mailman-hyperkitty
Summary:        Mailman archiver plugin for HyperKitty
%description -n python3-mailman-hyperkitty

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir mailman-hyperkitty-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
install -D -m 644 mailman-hyperkitty.cfg \
    %{buildroot}%{_sysconfdir}/mailman3.d/hyperkitty.cfg
%oreon_autofiles python3-mailman-hyperkitty usr/lib/python3*/site-packages/mailman_hyperkitty* usr/lib64/python3*/site-packages/mailman_hyperkitty* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/mailman_hyperkitty* usr/lib64/python3*/site-packages/mailman_hyperkitty* usr/bin/*

%check

%pyproject_check_import
touch nntplib.py
%{py3_test_envvars} %{python3} -m nose2 -v
rm nntplib.py
%files
%files -n python3-mailman-hyperkitty -f %{oreon_filedir}/python3-mailman-hyperkitty.list

%changelog

%autochangelog
