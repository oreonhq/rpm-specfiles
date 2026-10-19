%global source2_hash 81aab9440549501014c9f3546f68bd2e3e56774c782c530d298eb899f82b800b
%global source0_hash 36f286d93fa6b6bf7885f4899c997894d21da3a62176592ac162d9c6a8644f9e
Name:          jigdo
Version:       0.8.2
Release:        1%{?dist}
Summary:        Ease distribution of large files over the Internet
License:       GPL-2.0-only WITH x11vnc-openssl-exception
URL:           https://www.einval.com/~steve/software/jigdo/
Source0:        https://www.einval.com/~steve/software/%{name}/download/%{name}-%{version}.tar.xz
Source1:       %{url}download/%{name}-%{version}.tar.xz.sig
Source2:       https://www.einval.com/~steve/pgp/587979573442684E.asc
Source3:       jigdo.desktop
Patch:         %{name}-0.8.1-fix-docs.patch
Requires:      wget
# oreon:deps
BuildRequires:  bzip2-devel
BuildRequires:  curl-devel
BuildRequires:  docbook-utils
BuildRequires:  gawk
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gnupg2
BuildRequires:  libdb-devel
BuildRequires:  make
BuildRequires:  wget
BuildRequires:  zlib-devel
# /oreon:deps
%description

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

# don't clobber -g from C*FLAGS
sed -i '/.*echo "$C.*FLAGS"/d' configure

%build

export LDFLAGS="$LDFLAGS -lpthread"
%configure --with-libdb=-ldb
make # not SMP safe
%install
%make_install
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
