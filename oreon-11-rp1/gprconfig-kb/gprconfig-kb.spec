%global source0_hash ae6b4ee55e44d95bb7b581fe5f1497d2d3298856784cb34f4fce98ab71c3d864

# The testsuite is normally run. It can be disabled with "--without=check".
%bcond check 0

# Upstream source information.
%global upstream_owner    AdaCore
%global upstream_name     gprconfig_kb
%global upstream_version  26.0.0
%global upstream_commit   72c8aca4324a736a434d985ba1d02f5665e33355

Name:           gprconfig-kb
Version:        %{upstream_version}
Release:        2%{?dist}
Summary:        GNAT project configuration knowledge base
BuildArch:      noarch

License:        GPL-3.0-or-later WITH GCC-exception-3.1

URL:            https://github.com/%{upstream_owner}/%{upstream_name}
Source0:        %{url}/archive/%{upstream_commit}.tar.gz#/%{upstream_name}-%{upstream_version}.tar.gz

# [Fedora specific]
Source1:        fedora_arches.xml
Source2:        fedora_ar.xml

# [specific to recent GCC] Make detection of GCC compilers independent of locale.
Patch1:         %{name}-improve-detection-of-gcc.patch
# Our guess at why Adacore don't do this is that they might want to support old
# versions of GCC that lack -dumpfullversion.

# [Unix-specific] Make detection of GNU ld independent of locale.
Patch2:         %{name}-improve-detection-of-gnu-ld.patch
# Use of env makes this patch specific to Unix-like systems.

# [specific to recent Clang] Make detection of Clang compilers independent of locale.
Patch3:         %{name}-improve-detection-of-clang.patch
# Our guess at why Adacore don't do this is that they might want to support old
# versions of Clang where -dumpversion returns a hardcoded fake version number.

%if %{with check}
# The XML files are checked with XMLlint. Using a tool not written in Ada for
# this avoids a dependency loop that would make bootstrapping GPRbuild even
# more complicated. The checking can be disabled if there should be a problem
# with this dependency.
BuildRequires:  libxml2
%endif

# The contents of this package are split off from the gprbuild package.
Conflicts:      gprbuild <= 2020

%description
The GNAT project configuration knowledge base is used for configuring
GNAT project toolchains.

#############
## Prepare ##
#############

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -C -p1

###########
## Build ##
###########

%build
%nil

#############
## Install ##
#############

%install
%global inst install --mode=u=rw,go=r,a-s --preserve-timestamps

mkdir --parents %{buildroot}%{_datadir}/gprconfig
%{inst} --target-directory=%{buildroot}%{_datadir}/gprconfig db/gprconfig.xsd
%{inst} --target-directory=%{buildroot}%{_datadir}/gprconfig db/*.xml
%{inst} --target-directory=%{buildroot}%{_datadir}/gprconfig db/*.ent
%{inst} --target-directory=%{buildroot}%{_datadir}/gprconfig %{SOURCE1} %{SOURCE2}

###########
## Check ##
###########

%if %{with check}
%check
# Check that the XML files are valid according to the XML schema.
xmllint --nonet --noout --noent \
        --schema %{buildroot}%{_datadir}/gprconfig/gprconfig.xsd \
        %{buildroot}%{_datadir}/gprconfig/*.xml
# --schema requires --noent when the XML files contain entity references.
%endif

###########
## Files ##
###########

%files
%license COPYING3 COPYING.RUNTIME
%doc README*
%{_datadir}/gprconfig

###############
## Changelog ##
###############

%changelog
%autochangelog
