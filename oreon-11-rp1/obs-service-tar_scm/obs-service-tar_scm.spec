%global source0_hash 5b30f448b6eb4a55a7af6ec6e8c5fa20aba3f1d34cdd8028821f9f55e7ddd803

%define service tar_scm

Name:           obs-service-%{service}
Version:        0.10.41
Release:        5%{?dist}
Summary:        An OBS source service: checkout or update a tarball from svn/git/hg
License:        GPL-2.0-or-later
URL:            https://github.com/openSUSE/%{name}
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  glibc-langpack-en
BuildRequires:  python3-six
BuildRequires:  bzr
BuildRequires:  git-core
BuildRequires:  gnupg2
BuildRequires:  mercurial
BuildRequires:  subversion

BuildRequires:  python3-PyYAML
BuildRequires:  python3-dateutil
BuildRequires:  python3-lxml

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       obs-service-obs_scm-common = %{version}-%{release}

BuildArch:      noarch

%description
This is a source service for openSUSE Build Service.

It supports downloading from svn, git, hg and bzr repositories.

%package -n     obs-service-obs_scm-common
Summary:        Common parts of SCM handling services
Requires:       (glibc-langpack-en or glibc-all-langpacks)
Requires:       python3-PyYAML
Requires:       python3-dateutil
Requires:       git-core
Requires:       gnupg2
Requires:       obs-service-download_files
# Ensure that the interpreter is installed
Requires:       /usr/bin/python3
Recommends:     bzr
Recommends:     mercurial
Recommends:     subversion

%description -n obs-service-obs_scm-common
This is a source service for openSUSE Build Service.

It supports downloading from svn, git, hg and bzr repositories.

This package holds the shared files for different services.

%package -n     obs-service-tar
Summary:        Creates a tar archive from local directory
Requires:       obs-service-obs_scm-common = %{version}-%{release}

%description -n obs-service-tar
Creates a tar archive from local directory

%package -n     obs-service-obs_scm
Summary:        Creates a OBS cpio from a remote SCM resource
Requires:       obs-service-obs_scm-common = %{version}-%{release}

%description -n obs-service-obs_scm
Creates a OBS cpio from a remote SCM resource.

This can be used to work directly in local git checkout and can be packaged
into a tar ball during build time.

%package -n     obs-service-appimage
Summary:        Handles source downloads defined in appimage.yml files
Requires:       obs-service-obs_scm-common = %{version}-%{release}

%description -n obs-service-appimage
Experimental appimage support: This parses appimage.yml files for SCM
resources and packages them.

%package -n     obs-service-snapcraft
Summary:        Handles source downloads defined in snapcraft.yaml files
Requires:       obs-service-obs_scm-common = %{version}-%{release}

%description -n obs-service-snapcraft
Experimental snapcraft support: This parses snapcraft.yaml files for SCM
resources and packages them.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
# Nothing to build

%install
%make_install PREFIX="%{_prefix}" SYSCFG="%{_sysconfdir}" PYTHON="%{__python3}"
%py_byte_compile %{__python3} %{buildroot}%{_prefix}/lib/obs/service/TarSCM

%check
# No need to run PEP8 tests here; that would require a potentially
# brittle BuildRequires: python3-pep8, and any style issues are already
# caught by Travis CI.
make test3

%files
%{_prefix}/lib/obs/service/tar_scm.service

%files -n obs-service-obs_scm-common
%license COPYING
%doc README.md
%dir %{_prefix}/lib/obs
%dir %{_prefix}/lib/obs/service
%{_prefix}/lib/obs/service/TarSCM
%{_prefix}/lib/obs/service/tar_scm
%dir %{_sysconfdir}/obs
%dir %{_sysconfdir}/obs/services
%config(noreplace) %{_sysconfdir}/obs/services/*

%files -n obs-service-tar
%{_prefix}/lib/obs/service/tar
%{_prefix}/lib/obs/service/tar.service

%files -n obs-service-obs_scm
%{_prefix}/lib/obs/service/obs_scm
%{_prefix}/lib/obs/service/obs_scm.service

%files -n obs-service-appimage
%{_prefix}/lib/obs/service/appimage*

%files -n obs-service-snapcraft
%{_prefix}/lib/obs/service/snapcraft*

%changelog
%autochangelog
