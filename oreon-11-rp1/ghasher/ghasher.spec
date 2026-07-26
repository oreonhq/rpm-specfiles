%global source0_hash 795d18ecd0af6037239c07a8d12ccfaeda7d87aed07dc7d9168da471e3e24d5b

Name:           ghasher
Version:        1.2.1
Release:        44%{?dist}
Summary:        GUI hasher for GTK+ 2
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://asgaard.homelinux.org/code/ghasher/
Source0:        http://asgaard.homelinux.org/code/ghasher/ghasher-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  gtk2-devel >= 2.4 openssl-devel desktop-file-utils libglade2-devel
BuildRequires: make
Patch0:         %{name}-format-security.patch
Patch1:         %{name}-openssl-1.1.0.patch

%description
ghasher can easily show the MD5 sum (or md2, md4, sha1, sha, ripemd160, dss1)
of a file. Motivation for this utility was that users shouldn't need to open a
command line for checking the MD5 sum of files they download.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%make_build

%install
#make_install
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

%files
%doc AUTHORS NEWS README TODO
%license LICENSE
%{_bindir}/*
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/pixmaps/*

%changelog
%autochangelog
