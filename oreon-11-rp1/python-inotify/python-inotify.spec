# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 9c998a5d7606ca835065cdabc013ae6c66eb9ea76a00a1e3bc6e0cfe2b4f71f4
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%global oname  pyinotify

Summary:       Monitor filesystem events with Python under Linux
Name:          python-inotify
Version:       0.9.6
Release:       43%{?dist}
License:       MIT
URL:           https://github.com/seb-m/pyinotify
Source0:       http://seb.dbzteam.org/pub/pyinotify/releases/pyinotify-%{version}.tar.gz
Patch:         pyinotify-0.9.6-epoint.patch
# Upstream pull request https://github.com/seb-m/pyinotify/pull/205
# Upstream issue https://github.com/seb-m/pyinotify/issues/204
Patch:         pyinotify-python-3.12-fix.patch
BuildRequires: gmp-devel
BuildRequires: python%{python3_pkgversion}-devel
BuildArch:     noarch
%global _description \
This is a Python module for watching filesystems changes. pyinotify \
can be used for various kind of fs monitoring. Based on inotify which \
is an event-driven notifier, where notifications are exported from \
kernel space to user space.
%description %_description

%package    -n python%{python3_pkgversion}-inotify
Summary:       %{summary}
%description -n python%{python3_pkgversion}-inotify %_description

%prep
%oreon_verify_sources
%autosetup -p1 -n %{oname}-%{version}
sed -i '1c#! %{__python3}' python3/pyinotify.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l '%{oname}*'

%check
%pyproject_check_import
%py3_check_import pyinotify

%files -n python%{python3_pkgversion}-inotify -f %{pyproject_files}
%doc ACKS README.md
%{_bindir}/%{oname}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.9.6-43
- Prepare for Oreon 11 (RP1)
