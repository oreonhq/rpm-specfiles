%global source0_hash 391b4070ed5e0a2f5583a6cfe967b68f8038047b88f0875c7f0500f4d96d1a8a
%define service tar_scm
Name:           obs-service-%{service}
Version:        0.13.0
Release:        1%{?dist}
Summary:        An OBS source service: checkout or update a tarball from svn/git/hg
License:        GPL-2.0-or-later
URL:            https://github.com/openSUSE/%{name}
Source0:        https://github.com/openSUSE/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Requires:       obs-service-obs_scm-common = %{version}-%{release}
BuildArch:      noarch
# oreon:deps
BuildRequires:  bzr
BuildRequires:  git-core
BuildRequires:  glibc-langpack-en
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  mercurial
BuildRequires:  python3-PyYAML
BuildRequires:  python3-dateutil
BuildRequires:  python3-devel
BuildRequires:  python3-lxml
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
BuildRequires:  subversion
# /oreon:deps
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
%oreon_prep
%build

%install
%make_install PREFIX="%{_prefix}" SYSCFG="%{_sysconfdir}" PYTHON="%{__python3}"
%py_byte_compile %{__python3} %{buildroot}%{_prefix}/lib/obs/service/TarSCM
%oreon_autofiles obs-service-obs_scm-common usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles obs-service-tar usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles obs-service-obs_scm usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles obs-service-appimage usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles obs-service-snapcraft usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test3
%files -f %{oreon_filedir}/main.list
%files -n obs-service-obs_scm-common -f %{oreon_filedir}/obs-service-obs_scm-common.list
%files -n obs-service-tar -f %{oreon_filedir}/obs-service-tar.list
%files -n obs-service-obs_scm -f %{oreon_filedir}/obs-service-obs_scm.list
%files -n obs-service-appimage -f %{oreon_filedir}/obs-service-appimage.list
%files -n obs-service-snapcraft -f %{oreon_filedir}/obs-service-snapcraft.list

%changelog

%autochangelog
