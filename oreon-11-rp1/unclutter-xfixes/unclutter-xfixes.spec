%global source0_hash 6f7f248f16b7d4ec7cb144b6bc5a66bd49078130513a184f4dc16c498d457db9

Name: unclutter-xfixes
Version: 1.6
Release: 9%{?dist}
Summary: Hides the cursor on inactivity (rewrite of unclutter)
License: MIT
URL: https://github.com/Airblader/unclutter-xfixes
Provides: unclutter = %{version}-%{release}
Source0: https://github.com/Airblader/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: asciidoc
BuildRequires: gcc
BuildRequires: git
BuildRequires: libX11-devel
BuildRequires: libXi-devel
BuildRequires: libev-devel
BuildRequires: make

%description
This is a rewrite of the popular tool unclutter, but using the
x11-xfixes extension. This means that this rewrite doesn't use fake windows or
pointer grabbing and hence causes less problems with window managers and/or
applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S git_am

%build
make %{?_smp_mflags} CFLAGS="%{optflags} %{build_ldflags}"

%install
%make_install
rm -r %{buildroot}%{_prefix}/share/licenses

%files
%license LICENSE
%{_bindir}/unclutter
%{_mandir}/man1/unclutter.1*

%changelog
%autochangelog
