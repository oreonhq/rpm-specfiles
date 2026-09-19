%global source0_hash d5db24765812e506b0c3f621e8c46489763082d852aa96aea1d8ba82053186fb

%global  framework kross-interpreters
%global  kross_ruby 1
%global  kross_java 0
%if 0%{?rhel} && 0%{?rhel} < 9
%global  kross_python2 1
%endif

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kf5-kross-interpreters
Summary: Kross interpreters for KDE Frameworks 5
Version: 22.04.3
Release: 15%{?dist}

License: LGPL-2.1-or-later AND CC0-1.0
URL:     https://invent.kde.org/frameworks/%{framework}

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/release-service/%{version}/src/%{framework}-%{version}.tar.xz

## FIXME: rebase or drop -- rdieter
# Fix Ruby 3.0 FTBFS
# https://invent.kde.org/libraries/kross-interpreters/-/merge_requests/1
#Patch0: kross-interpreters-20.08.3-Drop-safe-level-support-in-more-recent-Rubies.patch

%if 0%{?kross_ruby}
BuildRequires: ruby-devel ruby
%endif

%if 0%{?kross_java}
BuildRequires: java-devel
%endif

%if 0%{?kross_python2}
BuildRequires:  python2-devel
%endif

BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-kdelibs4support-devel
BuildRequires:  kf5-kross-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  qt5-qtbase-devel

%description
%{summary}.

# named to match as an addon to kf5-kross
%package -n kf5-kross-python2
Summary:  KF5 Kross plugin for python2
Obsoletes: kf5-kross-python < 16.04
Provides:  kf5-kross-python = %{version}-%{release}
Provides: kf5kross(python2) = %{version}-%{release}
%description -n kf5-kross-python2
Python plugin for the Kross archtecture in KDE Frameworks 5.

# named to match as an addon to kf5-kross
%package -n kf5-kross-java
Summary:  KF5 Kross plugin for java
Provides: kf5kross(java) = %{version}-%{release}
%description -n kf5-kross-java
Java plugin for the Kross archtecture in KDE Frameworks 5.

# named to match as an addon to kf5-kross
%package -n kf5-kross-ruby
Summary:  KF5 Kross plugin for ruby
Provides: kf5kross(ruby) = %{version}-%{release}
%description -n kf5-kross-ruby
Ruby plugin for the Kross archtecture in KDE Frameworks 5.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version} -p1

%build
%{cmake_kf5}
%cmake_build

%install
%cmake_install

%if 0%{?kross_python2}
%files -n kf5-kross-python2
%license COPYING
%{_kf5_qtplugindir}/krosspython.so
%endif

%if 0%{?kross_java}
%files -n kf5-kross-java
%license COPYING
%{_kf5_qtplugindir}/kross/kross.jar
%{_kf5_qtplugindir}/krossjava.so
%endif

%if 0%{?kross_ruby}
%files -n kf5-kross-ruby
%license COPYING
%{_kf5_qtplugindir}/krossruby.so
%endif

%changelog
%autochangelog
