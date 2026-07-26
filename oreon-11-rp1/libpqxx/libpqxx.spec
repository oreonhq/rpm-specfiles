%global source0_hash aa214df8b98672a43a39b68a37da87af1415a44965f6e484f85ca0eb4f151367

%bcond check 1
%bcond doc   1

Name:           libpqxx
Summary:        C++ client API for PostgreSQL
Epoch:          1
Version:        7.10.5
Release:        2%{?dist}

%global         forgeurl https://github.com/jtv/%{name}/
%global         tag %{version}
%forgemeta

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://pqxx.org/
Source0:        %{forgesource}

# Add missing includes for std::optional and std::variant.
Patch0:         libpqxx-7.10.5-cxx20.patch

BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  libpq-devel
%if %{with check}
BuildRequires:  postgresql-test-rpm-macros
%endif
%if %{with doc}
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  xmlto
%endif

%description
C++ client API for PostgreSQL. The standard front-end (in the sense of
"language binding") for writing C++ programs that use PostgreSQL.
Supersedes older libpq++ interface.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       pkgconfig
%description devel
%{summary}.

%if %{with doc}
%package doc
Summary: Developer documentation for %{name}
BuildArch: noarch
%description doc
%{summary}.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build
%cmake -G Ninja \
%if %{with doc}
  -DBUILD_DOC=ON
%endif
%cmake_build

%install
%cmake_install

%check
%if %{with check}
%postgresql_tests_run
cd "%{_vpath_builddir}/test"
%__ctest -V --force-new-ctest-process %{?_smp_mflags}
cd -
%endif

%files
%doc AUTHORS NEWS README.md VERSION
%license COPYING
%{_libdir}/%{name}-7.10.so

%files devel
%dir %{_libdir}/cmake/%{name}
%{_includedir}/pqxx
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}/%{name}-config.cmake
%{_libdir}/cmake/%{name}/%{name}-config-version.cmake
%{_libdir}/cmake/%{name}/%{name}-targets.cmake
%{_libdir}/cmake/%{name}/%{name}-targets-noconfig.cmake

%if %{with doc}
%files doc
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/accessing-results.md
%{_docdir}/%{name}/binary-data.md
%{_docdir}/%{name}/datatypes.md
%{_docdir}/%{name}/escaping.md
%{_docdir}/%{name}/getting-started.md
%{_docdir}/%{name}/mainpage.md
%{_docdir}/%{name}/parameters.md
%{_docdir}/%{name}/performance.md
%{_docdir}/%{name}/prepared-statement.md
%{_docdir}/%{name}/streams.md
%{_docdir}/%{name}/thread-safety.md
%{_docdir}/%{name}/html
%endif

%changelog
%autochangelog
