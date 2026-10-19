%global source1_hash c9bff75738922193e67fa726fa225535870d2aa1059f91452c411736284ad566
%global source0_hash 32173746e2621b839de7e43edcb1dd10e266f73fae1a3a6b1ec3ceb7fa5622e3
%global commit b795c03b1982964fb91ffd57ce8112844efd3291
%global snapdate 20240120
Name:           cr-marcstevens-snippets
%global snapinfo ^%{snapdate}git%{sub %{commit} 1 7}
Version:        0%{snapinfo}
Release:        1%{?dist}
Summary:        Collection of useful one-file C/C++ headers
License:        MIT AND BSL-1.0
SourceLicense:  %{shrink:
                %{license} AND
                FSFAP AND
                GPL-3.0-or-later WITH Autoconf-exception-macro AND
                GPL-2.0-or-later WITH Autoconf-exception-generic
                }
URL:            https://github.com/cr-marcstevens/snippets
Source0:        https://github.com/cr-marcstevens/snippets/archive/%{commit}/snippets-%{commit}.tar.gz
Source1:        https://www.boost.org/LICENSE_1_0.txt
Patch:          %{url}/pull/2.patch
%global debug_package %{nil}
# oreon:deps
BuildRequires:  gcc-c++
# /oreon:deps
%description
%{summary}.

%package base64-devel
Summary:        A header only C++ base64 encoder/decoder library
License:        MIT
BuildArch:      noarch
Provides:       %{name}-base64-static = %{?epoch:%{epoch}:}%{version}-%{release}
%description base64-devel
%{summary}.

%package concurrent_unordered_map-devel
Summary:        A header only C++ light-weight concurrent unordered map
License:        MIT
BuildArch:      noarch
Provides:       %{name}-concurrent_unordered_map-static = %{?epoch:%{epoch}:}%{version}-%{release}
%description concurrent_unordered_map-devel
%{summary}.

%package cpuperformance-devel
Summary:        A header only C++ light-weight aids for CPU cycle counting
License:        MIT
BuildArch:      noarch
Provides:       %{name}-cpuperformance-static = %{?epoch:%{epoch}:}%{version}-%{release}
%description cpuperformance-devel
%{summary}.

%package parallel_algorithms-devel
Summary:        A header only C++ light-weight parallel algorithms library
License:        MIT
BuildArch:      noarch
Provides:       %{name}-parallel_algorithms-static = %{?epoch:%{epoch}:}%{version}-%{release}
%description parallel_algorithms-devel
%{summary}.

%package program_options-devel
Summary:        A header only C++ C++ boost-like program options class
License:        MIT
BuildArch:      noarch
Provides:       %{name}-program_options-static = %{?epoch:%{epoch}:}%{version}-%{release}
%description program_options-devel
%{summary}.

%package progress_display-devel
Summary:        Extension from boost::progress_display
License:        BSL-1.0
BuildArch:      noarch
Provides:       %{name}-progress_display-static = %{?epoch:%{epoch}:}%{version}-%{release}
%description progress_display-devel
%{summary}.

%package string_algo-devel
Summary:        A header only C++ string algorithms
License:        MIT
BuildArch:      noarch
Provides:       %{name}-string_algo-static = %{?epoch:%{epoch}:}%{version}-%{release}
%description string_algo-devel
%{summary}.

%package thread_pool-devel
Summary:        A header only C++ light-weight thread pool
License:        MIT
BuildArch:      noarch
Provides:       %{name}-thread_pool-static = %{?epoch:%{epoch}:}%{version}-%{release}
%description thread_pool-devel
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n snippets-%{commit} -p1
# We are not packaging these, and many have licenses that are acceptable for
# packaging but differ from those listed in the License field. To keep things
# clean, we remove them.
rm -rvf autoconf
# Please add Boost license text
# https://github.com/cr-marcstevens/snippets/issues/3
cp -p '%{SOURCE1}' .

%build

%set_build_flags
mkdir -p _test '%{_vpath_builddir}'
for hdr in cxxheaderonly/*.hpp
do
  lib="$(basename "${hdr}" '.hpp')"
  cat > "_test/${lib}.cpp" <<EOF
int main(int, char *[]) { return 0; }
EOF
  "${CXX:-g++}" -I"${PWD}/cxxheaderonly" "_test/${lib}.cpp" \
      -o "%{_vpath_builddir}/${lib}" ${CXXFLAGS} ${LDFLAGS}
done
%install
install -t '%{buildroot}%{_includedir}/cr-marcstevens' \
    -p -m 0644 -D cxxheaderonly/*.hpp
%oreon_autofiles cr-marcstevens-snippets-base64-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles cr-marcstevens-snippets-concurrent_unordered_map-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles cr-marcstevens-snippets-cpuperformance-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles cr-marcstevens-snippets-parallel_algorithms-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles cr-marcstevens-snippets-program_options-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles cr-marcstevens-snippets-progress_display-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles cr-marcstevens-snippets-string_algo-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles cr-marcstevens-snippets-thread_pool-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n cr-marcstevens-snippets-base64-devel -f %{oreon_filedir}/cr-marcstevens-snippets-base64-devel.list
%files -n cr-marcstevens-snippets-concurrent_unordered_map-devel -f %{oreon_filedir}/cr-marcstevens-snippets-concurrent_unordered_map-devel.list
%files -n cr-marcstevens-snippets-cpuperformance-devel -f %{oreon_filedir}/cr-marcstevens-snippets-cpuperformance-devel.list
%files -n cr-marcstevens-snippets-parallel_algorithms-devel -f %{oreon_filedir}/cr-marcstevens-snippets-parallel_algorithms-devel.list
%files -n cr-marcstevens-snippets-program_options-devel -f %{oreon_filedir}/cr-marcstevens-snippets-program_options-devel.list
%files -n cr-marcstevens-snippets-progress_display-devel -f %{oreon_filedir}/cr-marcstevens-snippets-progress_display-devel.list
%files -n cr-marcstevens-snippets-string_algo-devel -f %{oreon_filedir}/cr-marcstevens-snippets-string_algo-devel.list
%files -n cr-marcstevens-snippets-thread_pool-devel -f %{oreon_filedir}/cr-marcstevens-snippets-thread_pool-devel.list

%changelog

%autochangelog
