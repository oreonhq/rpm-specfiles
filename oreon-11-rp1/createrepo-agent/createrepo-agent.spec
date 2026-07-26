%global source0_hash 8e4f89e69f18b984cbe8b0318cebe03d9cf53e6c8c7d612dc908e1d02e2cdf1c

Name:           createrepo-agent
Version:        0.5.1
Release:        1%{?dist}
Summary:        Rapidly and repeatedly generate RPM repository metadata

License:        Apache-2.0
URL:            https://github.com/osrf/createrepo-agent
Source0:        https://github.com/osrf/createrepo-agent/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  cmake(GTest)
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(createrepo_c)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gpg-error)
BuildRequires:  pkgconfig(gpgme)
BuildRequires:  pkgconfig(libassuan)
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}

%description
createrepo-agent is a tool for rapidly iterating on clusters of associated
RPM repositories. It leverages Assuan IPC to create a daemon process which
caches the metadata for each sub-repository in the cluster so that it
doesn't need to be re-loaded and parsed each time a change is made. The
most notable implementation of the Assuan protocol is gpg-agent, which
gives createrepo-agent its name.

%package -n python3-createrepo-agent
Summary:        %{summary}
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

%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc README.md TODO.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%files -n python3-createrepo-agent
%{python3_sitearch}/createrepo_agent.so
%{python3_sitearch}/createrepo_agent-%{version}.dist-info/

%changelog
%autochangelog
