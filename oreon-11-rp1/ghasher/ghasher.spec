%global source0_hash 795d18ecd0af6037239c07a8d12ccfaeda7d87aed07dc7d9168da471e3e24d5b
Name:           ghasher
Version:        1.2.1
Release:        44%{?dist}
Summary:        GUI hasher for GTK+ 2
License:        LicenseRef-Callaway-BSD
URL:            http://asgaard.homelinux.org/code/ghasher/
Source0:        http://asgaard.homelinux.org/code/ghasher/ghasher-%{version}.tar.gz
Patch0:         %{name}-format-security.patch
Patch1:         %{name}-openssl-1.1.0.patch
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gtk2-devel
BuildRequires:  libglade2-devel
BuildRequires:  make
BuildRequires:  openssl-devel
# /oreon:deps
%description
ghasher can easily show the MD5 sum (or md2, md4, sha1, sha, ripemd160, dss1)
of a file. Motivation for this utility was that users shouldn't need to open a
command line for checking the MD5 sum of files they download.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build
%install
install -D -m 0755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -D -m 0644 hash.xpm $RPM_BUILD_ROOT%{_datadir}/pixmaps/hash.xpm
cat > %{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=MD5 Sum Utility
Comment=Calculate the md5 sum of a file
Exec=ghasher %%F
Terminal=false
Type=Application
Icon=hash
Categories=Utility;GTK;Application;
EOF
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{name}.desktop
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
