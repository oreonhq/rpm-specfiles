%global source0_hash a6fba11f4460854267c610f066c185e859d7177699b50ef584fc4f705962d356
Name:    whipper
Version: 0.10.0
Release:        1%{?dist}
Summary:        Python CD-DA ripper preferring accuracy over speed
URL:     https://github.com/whipper-team/whipper
License: GPL-3.0-or-later
Source0:        https://github.com/whipper-team/%{name}/archive/v%{version}.tar.gz
Patch:         https://patch-diff.githubusercontent.com/raw/whipper-team/whipper/pull/543.patch
Requires: cdrdao
Requires: flac
Requires: libcdio-paranoia
Requires: python3dist(discid)
Requires: python3dist(musicbrainzngs)
Requires: python3dist(mutagen)
Requires: python3dist(pycdio)
Requires: python3dist(pygobject)
Requires: python3dist(ruamel-yaml)
Requires: sox
ExcludeArch: s390x
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-whipper = %{version}-%{release}
# /oreon:deps
%description
CD ripper preferring accuracy over speed

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel
%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install
%if "%_metainfodir" != "%{_datadir}/metainfo"
mv %{buildroot}%{_datadir}/metainfo/ \
   %{buildroot}%{_metainfodir}/
%endif
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/com.github.whipper_team.Whipper.metainfo.xml
%oreon_autofiles main

%check

%pyproject_check_import
%files

%changelog

%autochangelog
