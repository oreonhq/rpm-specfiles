%global source0_hash ae6b4ee55e44d95bb7b581fe5f1497d2d3298856784cb34f4fce98ab71c3d864
%bcond check 0
%global upstream_owner    AdaCore
%global upstream_name     gprconfig_kb
%global upstream_version  26.0.0
%global upstream_commit   72c8aca4324a736a434d985ba1d02f5665e33355
Name:           gprconfig-kb
Version:        %{upstream_version}
Release:        1%{?dist}
Summary:        GNAT project configuration knowledge base
BuildArch:      noarch
License:        GPL-3.0-or-later WITH GCC-exception-3.1
URL:            https://github.com/%{upstream_owner}/%{upstream_name}
Source0:        https://github.com/%{upstream_owner}/%{upstream_name}/archive/%{upstream_commit}.tar.gz#/%{upstream_name}-%{version}.tar.gz
Source1:        fedora_arches.xml
Source2:        fedora_ar.xml
Patch1:         %{name}-improve-detection-of-gcc.patch
Patch2:         %{name}-improve-detection-of-gnu-ld.patch
Patch3:         %{name}-improve-detection-of-clang.patch
%if %{with check}
%endif
Conflicts:      gprbuild <= 2020
# oreon:deps
BuildRequires:  libxml2
# /oreon:deps
%description
The GNAT project configuration knowledge base is used for configuring
GNAT project toolchains.

#############
## Prepare ##
#############

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{upstream_name}-%{upstream_commit}

###########
## Build ##
###########

%build

%nil
%install
%global inst install --mode=u=rw,go=r,a-s --preserve-timestamps
mkdir --parents %{buildroot}%{_datadir}/gprconfig
%{inst} --target-directory=%{buildroot}%{_datadir}/gprconfig db/gprconfig.xsd
%{inst} --target-directory=%{buildroot}%{_datadir}/gprconfig db/*.xml
%{inst} --target-directory=%{buildroot}%{_datadir}/gprconfig db/*.ent
%{inst} --target-directory=%{buildroot}%{_datadir}/gprconfig %{SOURCE1} %{SOURCE2}
%oreon_autofiles main
%if %{with check}
%check

xmllint --nonet --noout --noent \
        --schema %{buildroot}%{_datadir}/gprconfig/gprconfig.xsd \
        %{buildroot}%{_datadir}/gprconfig/*.xml
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
