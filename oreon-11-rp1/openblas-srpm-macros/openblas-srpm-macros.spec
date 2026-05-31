%global source0_hash none

Name:           openblas-srpm-macros
Version:        2
Release:        21%{?dist}
Summary:        OpenBLAS architecture macros
License:        MIT
Source0:        macros.openblas-srpm
BuildArch:      noarch

%description
%{summary}.


%prep


test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%build


%install
%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)
mkdir -p %{buildroot}%{macrosdir}
install -m0644 %SOURCE0 %{buildroot}%{macrosdir}/macros.openblas-srpm


%files
%{macrosdir}/macros.openblas-srpm


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2-21
- Import
