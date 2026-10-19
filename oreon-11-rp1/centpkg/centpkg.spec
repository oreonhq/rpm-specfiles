%global source0_hash 0952cd77b9d0869d4c7cf2adef76130459541425c1f1b2bef0e287e51a27e71e
%if %{defined el8}
%global __python3 %{_libexecdir}/platform-python
%endif
Name:           centpkg
Version:        0.10.3
Release:        1%{?dist}
Summary:        CentOS utility for working with dist-git
License:        GPL-2.0-or-later
URL:            https://gitlab.com/CentOS/common/centpkg
Source0:        https://gitlab.com/CentOS/common/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Conflicts:      streamkoji < 1.1-3
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-centpkg = %{version}-%{release}
# /oreon:deps
%description
Provides the centpkg command for working with dist-git.

%package sig
Summary:        CentOS SIG utility for working with dist-git
Requires:       %{name} = %{version}-%{release}
%description sig
Provides the centpkg-sig command for working with dist-git.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%{python3} doc/centpkg_man_page.py > centpkg.1
%install
%pyproject_install
install -D -p -m 0644 src/stream.conf      %{buildroot}%{_sysconfdir}/koji.conf.d/stream.conf
install -D -p -m 0644 src/centpkg.conf     %{buildroot}%{_sysconfdir}/rpkg/centpkg.conf
install -D -p -m 0644 src/centpkg-sig.conf %{buildroot}%{_sysconfdir}/rpkg/centpkg-sig.conf
install -D -p -m 0644 src/centpkg.bash     %{buildroot}%{_datadir}/bash-completion/completions/centpkg
install -D -p -m 0644 centpkg.1            %{buildroot}%{_mandir}/man1/centpkg.1
%oreon_autofiles centpkg-sig usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pyproject_check_import
PYTHONPATH=%{buildroot}%{python3_sitelib} %{python3} -m unittest discover --verbose
%files
%files -n centpkg-sig -f %{oreon_filedir}/centpkg-sig.list

%changelog

%autochangelog
