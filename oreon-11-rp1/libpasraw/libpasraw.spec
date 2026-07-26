%global source0_hash 108a324450932fb8c6c84193e8bb3b45c6b3db9e7b757acf986c33d0b4ddf40c

%global forgeurl https://github.com/pchev/libpasraw/

Version:        1.3.0
%forgemeta

Name:           libpasraw
Release:        %autorelease
Summary:        Pascal interface to libraw

License:        GPL-3.0-or-later
URL:            %{forgeurl}
Source0:        %{forgesource}

# Patch to fix stripping of library files
# Since this is Fedora specific we don't ask upstream to include
Patch0:         libpasraw-1.3-nostrip.patch

# Add LDFLAGS to compiler
Patch1:         libpasraw-1.3-ldflags.patch

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libraw)
BuildRequires: make

%description
Provides shared library to interface Pascal program with libraw.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# do not install docs, use %%doc macro
sed -i '/\$destdir\/share/d' ./install.sh

# fix library path in install.sh script on 64bit
sed -i 's/\$destdir\/lib/\$destdir\/%{_lib}/g' ./install.sh

%build
%make_build arch_flags="%{optflags}" LDFLAGS="%{build_ldflags}"

%install
make install PREFIX=%{buildroot}%{_prefix}

%files
%license LICENSE
%doc changelog copyright README.md
%{_libdir}/%{name}.so.1
%{_libdir}/%{name}.so.1.1

%files devel
%{_libdir}/%{name}.so

%changelog
%autochangelog
