%global source0_hash 6db837e7bbaa7c72c5fd43ca5af04b1d370c5ce32367b9f6a1f7b49b2338c09a
%global __oreon_hwcaps_post_install %{nil}
%global _distro_extra_cflags %{nil}
%global _distro_extra_cxxflags %{nil}
%global _distro_extra_ldflags %{nil}

Name:           rhash
Version:        1.4.5
Release:        4%{?dist}
Summary:        Great utility for computing hash sums

License:        MIT
URL:            https://github.com/rhash/RHash
Source0:        https://github.com/rhash/RHash/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc

%description
RHash is a console utility for calculation  and verification of magnet links
and a wide range of hash sums like  CRC32,  MD4, MD5,  SHA1, SHA256, SHA512,
SHA3,   AICH,  ED2K,  Tiger,  DC++ TTH,  BitTorrent BTIH,   GOST R 34.11-94,
RIPEMD-160, HAS-160, EDON-R, Whirlpool and Snefru.

Hash sums are used to  ensure and verify integrity  of large volumes of data
for a long-term storing or transferring.

Features:
 * Output in a predefined (SFV, BSD-like) or a user-defined format.
 * Can calculate Magnet links.
 * Updating hash files (adding hash sums of files missing in the hash file).
 * Calculates several hash sums in one pass
 * Ability to process directories recursively.
 * Portability: the program works the same on Linux, *BSD or Windows.


%package        devel
Summary:        Development files for lib%{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
LibRHash is a professional,  portable,  thread-safe  C library for computing
a wide variety of hash sums, such as  CRC32, MD4, MD5, SHA1, SHA256, SHA512,
SHA3,   AICH,  ED2K,  Tiger,  DC++ TTH,  BitTorrent BTIH,   GOST R 34.11-94,
RIPEMD-160, HAS-160, EDON-R, Whirlpool and Snefru.
Hash sums are used  to ensure and verify integrity of  large volumes of data
for a long-term storing or transferring.

Features:
 * Small and easy to learn interface.
 * Hi-level and Low-level API.
 * Allows calculating of several hash functions simultaneously.
 * Portability: the library works on Linux, *BSD and Windows.

The %{name}-devel package contains libraries and header files for
developing applications that use lib%{name}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n RHash-%{version}
sed -i -e '/^INSTALL_SHARED/s/644/755/' librhash/Makefile


%build
INSTALL_INCDIR=%{_includedir} ./configure --sysconfdir=%{_sysconfdir} --exec-prefix=%{_prefix} --mandir=%{_mandir} --libdir=%{_libdir}
%make_build OPTFLAGS="%{optflags}" OPTLDFLAGS="-g %{?__global_ldflags}" build


%install
%make_install
make DESTDIR=%{buildroot} -C librhash install-so-link install-lib-headers


%check
make test-shared


%files
%license COPYING
%doc ChangeLog README.md
%config(noreplace) %{_sysconfdir}/rhashrc
%{_bindir}/*
%{_libdir}/*.so.1*
%{_mandir}/man1/*.1*

%files devel
%{_includedir}/*
%{_libdir}/*.so


%changelog
* Sat Apr 18 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.5-4
- Import for Oreon 11
