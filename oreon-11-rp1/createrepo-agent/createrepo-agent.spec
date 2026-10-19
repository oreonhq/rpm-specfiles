%global source0_hash 6438ca006d7c00ffb851f284949b8a0fcfe4c0d5c026b5742b39dcb9a5c005aa
Name:           createrepo-agent
Version:        0.6.0
Release:        1%{?dist}
Summary:        Rapidly and repeatedly generate RPM repository metadata
License:        Apache-2.0
URL:            https://github.com/osrf/createrepo-agent
Source0:        https://github.com/osrf/createrepo-agent/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(GTest)
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(createrepo_c)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gpg-error)
BuildRequires:  pkgconfig(gpgme)
BuildRequires:  pkgconfig(libassuan)
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
# /oreon:deps
%description
createrepo-agent is a tool for rapidly iterating on clusters of associated
RPM repositories. It leverages Assuan IPC to create a daemon process which
caches the metadata for each sub-repository in the cluster so that it
doesn't need to be re-loaded and parsed each time a change is made. The
most notable implementation of the Assuan protocol is gpg-agent, which
gives createrepo-agent its name.

%package -n python3-createrepo-agent
Summary:        Rapidly and repeatedly generate RPM repository metadata
Requires:       createrepo-agent%{?_isa} = %{version}-%{release}
%description -n python3-createrepo-agent
createrepo-agent is a tool for rapidly iterating on clusters of associated
RPM repositories. It leverages Assuan IPC to create a daemon process which
caches the metadata for each sub-repository in the cluster so that it
doesn't need to be re-loaded and parsed each time a change is made. The
most notable implementation of the Assuan protocol is gpg-agent, which
gives createrepo-agent its name.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles python3-createrepo-agent usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n python3-createrepo-agent -f %{oreon_filedir}/python3-createrepo-agent.list

%changelog

%autochangelog
