%global source0_hash none

%global _legacy_common_support 1
%global forgeurl https://gitlab.utu.fi/vesoik/tpcclib

Name:           libtpcmisc
# upstream has gone from versioning series 1.x to 0.x in the new GitLab repository
Epoch:          1
Version:        0.8.0
Release:        %autorelease
Summary:        Miscellaneous PET functions

# upstream only supports 64 bit architectures
ExcludeArch:    %{ix86}

%global tag  v%{version}

%forgemeta

License:        GPL-3.0-or-later
URL:            %forgeurl
Source0:        %forgesource

# fedora related changes are in my fork
# - generate shared objects
# - only build tpcmisc
# - clean up compiler flags
Patch:          https://gitlab.com/sanjayankur31/tpcclib/-/merge_requests/1.patch

BuildRequires:  cmake
BuildRequires:  git-core
BuildRequires:  gcc

%description
Former libpet, the common PET C library, has been divided up in 
smaller sub-libraries that each handle a specific task. 
This library includes miscellaneous functions utilized in PET 
data processing.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        static
Summary:        Static libraries for %{name}

%description    static
This package contains static libraries for %{name}.

%prep
%forgeautosetup -S git

sed -i 's/\r$//' changelog.md
sed -i 's/\r$//' readme.md

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license license.md
%doc readme.md changelog.md
%{_bindir}/%{name}
%{_libdir}/%{name}.so.0.0.0
%{_libdir}/%{name}.so.0

%files devel
%{_libdir}/%{name}.so
%{_includedir}/*

%files static
%license license.md
%{_libdir}/%{name}.a

%changelog
%autochangelog
