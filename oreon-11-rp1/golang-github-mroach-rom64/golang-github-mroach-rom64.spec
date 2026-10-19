%global source0_hash 1fe77647177e06efde11ce45dc28ddf78d859e558d94bc28b0aaf1783b94266c
%bcond check 0
%global goipath         github.com/mroach/rom64
Version:                0.5.3
%gometa
%global common_description %{expand:
Nintendo 64 ROM utility written in Go:
- List information about all ROMs in a directory
- Show information about a single ROM
- Convert a ROM file to the native (Z64, Big-endian) format
- Validate the ROM's SHA-1 checksum against a list of known-good ROM dumps.}
%global golicenses      LICENSE
%global godocs          doc rom_info.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Nintendo 64 ROM utility
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/rom64-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%package -n       rom64
Summary:        Nintendo 64 ROM utility
BuildArch:      noarch

%description -n rom64
Nintendo 64 ROM utility

%description
%{common_description}

%package -n     rom64
Summary:        Nintendo 64 ROM utility
%description -n rom64
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%build

%gobuild -o %{gobuilddir}/bin/rom64 %{goipath}
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles rom64 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list
%files -n rom64 -f %{oreon_filedir}/rom64.list

%changelog

%autochangelog
