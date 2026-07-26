%global source0_hash 0edaea2a9d9709d456aa99a1c3e17812ed130f9ef2b5c2d152c230a5cbc5c482

%global debug_package %{nil}

Name:           cppcodec
Version:        0.2
Release:        17%{?dist}
Summary:        Header-only C++11 library to encode/decode base64/base64url/base32/base32hex/hex

License:        MIT
URL:            https://github.com/tplgy/cppcodec
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake >= 3.12
BuildRequires:  gcc-c++
BuildRequires:  catch2-devel

%global _description \
Header-only C++11 library to encode/decode base64, base64url, base32, base32hex\
and hex (a.k.a. base16) as specified in RFC 4648, plus Crockford's base32.\
\
MIT licensed with consistent, flexible API. Supports raw pointers,\
std::string and (templated) character vectors without unnecessary allocations.

%description %{_description}

%package        devel
Summary:        %{summary}
Provides:       %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}

%description    devel %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# No bundled catch
rm -vrf test/catch

%build
%cmake -DBUILD_TESTING=TRUE
%cmake_build

%install
%cmake_install

%check
%ctest

%files devel
%license LICENSE
%doc README.md
%{_includedir}/%{name}/
%{_datadir}/pkgconfig/%{name}-1.pc

%changelog
%autochangelog
