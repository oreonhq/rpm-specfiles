%global source0_hash 7ab519b9d3a49f29a01a9aea52109a4af37f5a5996675aa01fc1c362b34e8362

%global octpkg dicom

Name:           octave-%{octpkg}
Version:        0.6.1
Release:        %autorelease
Summary:        Dicom processing for Octave
License:        GPL-3.0-or-later
URL:            https://gnu-octave.github.io/packages/dicom/
Source0:        https://downloads.sourceforge.net/project/octave/Octave%20Forge%20Packages/Individual%20Package%20Releases/%{octpkg}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  octave-devel
BuildRequires:  gdcm-devel
BuildRequires:  libappstream-glib

Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave

%description
The Octave-forge Image package provides functions for processing 
Digital communications in medicine (DICOM) files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{octpkg}-%{version}

%build
# Tell it where gdcm headers are
export GDCM_CXXFLAGS="-I%{_includedir}/gdcm/"
%octave_pkg_build

%install
%octave_pkg_install
# Remove unneeded files that depends on python
rm %{buildroot}%{octpkgdir}/doc/mk*.py

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%{octpkglibdir}
%{octpkgdir}/
%{_metainfodir}/%{name}.metainfo.xml

%changelog
%autochangelog
