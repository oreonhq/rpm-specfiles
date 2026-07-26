%global source0_hash ac1b1e23a0de93a57f15e4b4d802a539c524df483504cee5055d15c4dd6049e6

Name:           cmake-fedora
Version:        2.9.3
Release:        25%{?dist}
Summary:        CMake helper modules for fedora developers
License:        BSD-2-Clause-FreeBSD
URL:            https://pagure.io/%{name}/
Source0:        https://releases.pagure.org/%{name}/%{name}-%{version}-Source.tar.gz

BuildRequires:  cmake >= 2.6.2
BuildRequires:  koji
Requires:       cmake >= 2.6.2
Requires:       git
Requires:       bodhi-client
Requires:       koji
Requires:       rpm-build
Requires:       fedpkg
Requires:       fedora-packager
Requires:       curl

BuildArch:      noarch

%description
cmake-fedora consist a set of cmake modules that provides
helper macros and targets for fedora developers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}-Source

%build
# $RPM_OPT_FLAGS should be loaded from cmake macro.
%cmake -DCMAKE_FEDORA_ENABLE_FEDORA_BUILD=1 .
%cmake_build

%install
%cmake_install

# We install document using doc
rm -fr %{buildroot}%{_docdir}/*

%check
ctest --output-on-failure

%files
%doc AUTHORS README.md ChangeLog COPYING
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}-fedpkg
%{_bindir}/%{name}-koji
%{_bindir}/%{name}-newprj
%{_bindir}/%{name}-pkgdb
%{_bindir}/%{name}-reset
%{_bindir}/%{name}-zanata
%{_bindir}/koji-build-scratch
%{_datadir}/cmake/Modules/CmakeFedoraScript.cmake
%{_datadir}/cmake/Modules/DateTimeFormat.cmake
%{_datadir}/cmake/Modules/ManageAPIDoc.cmake
%{_datadir}/cmake/Modules/ManageArchive.cmake
%{_datadir}/cmake/Modules/ManageChangeLogScript.cmake
%{_datadir}/cmake/Modules/ManageDependency.cmake
%{_datadir}/cmake/Modules/ManageEnvironment.cmake
%{_datadir}/cmake/Modules/ManageEnvironmentCommon.cmake
%{_datadir}/cmake/Modules/ManageFile.cmake
%{_datadir}/cmake/Modules/ManageGConf.cmake
%{_datadir}/cmake/Modules/ManageGettextScript.cmake
%{_datadir}/cmake/Modules/ManageGitScript.cmake
%{_datadir}/cmake/Modules/ManageMessage.cmake
%{_datadir}/cmake/Modules/ManageRPM.cmake
%{_datadir}/cmake/Modules/ManageRPMScript.cmake
%{_datadir}/cmake/Modules/ManageRelease.cmake
%{_datadir}/cmake/Modules/ManageReleaseFedora.cmake
%{_datadir}/cmake/Modules/ManageSourceVersionControl.cmake
%{_datadir}/cmake/Modules/ManageString.cmake
%{_datadir}/cmake/Modules/ManageTarget.cmake
%{_datadir}/cmake/Modules/ManageTranslation.cmake
%{_datadir}/cmake/Modules/ManageUninstall.cmake
%{_datadir}/cmake/Modules/ManageUpload.cmake
%{_datadir}/cmake/Modules/ManageVariable.cmake
%{_datadir}/cmake/Modules/ManageVersion.cmake
%{_datadir}/cmake/Modules/ManageZanata.cmake
%{_datadir}/cmake/Modules/ManageZanataDefinition.cmake
%{_datadir}/cmake/Modules/ManageZanataScript.cmake
%{_datadir}/cmake/Modules/ManageZanataSuggest.cmake
%{_datadir}/cmake/Modules/cmake_uninstall.cmake.in
%{_datadir}/cmake/Templates/fedora/CMakeLists.txt.template
%{_datadir}/cmake/Templates/fedora/RELEASE-NOTES.txt.template
%{_datadir}/cmake/Templates/fedora/bsd-3-clauses.txt
%{_datadir}/cmake/Templates/fedora/gpl-2.0.txt
%{_datadir}/cmake/Templates/fedora/gpl-3.0.txt
%{_datadir}/cmake/Templates/fedora/lgpl-2.1.txt
%{_datadir}/cmake/Templates/fedora/lgpl-3.0.txt
%{_datadir}/cmake/Templates/fedora/project.spec.in

%changelog
%autochangelog
