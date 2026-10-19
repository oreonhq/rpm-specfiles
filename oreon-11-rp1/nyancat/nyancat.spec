%global source0_hash 88cdcaa9c7134503dd0364a97fa860da3381a09cb555c3aae9918360827c2032
Name:          nyancat
Version:       1.5.2
Release:        1%{?dist}
Summary:        Nyancat rendered in your terminal
License:       NCSA
URL:           https://github.com/klange/nyancat
Source0:        https://github.com/klange/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0001: 00-0001-Can-now-adjust-image-refresh-rate.patch
Patch0002: 01-0001-Converted-spaces-to-tabs-and-changed-to-setting-a-de.patch
# oreon:deps
BuildRequires:  gawk
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
Nyan Cat is the name of a YouTube video uploaded in April 2011, which became an
internet meme. The video merged a Japanese pop song with an animated cartoon
cat with a Pop-Tart for a torso, flying through space, and leaving a rainbow
trail behind it.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
awk '1;/\*\//{exit}' < src/nyancat.c > LICENSE

%build

%set_build_flags
make %{?_smp_mflags} nyancat
%install
mkdir -p %{buildroot}/%{_bindir}/
install -m 0755 src/nyancat %{buildroot}/%{_bindir}/
mkdir -p %{buildroot}/%{_mandir}/man1/
install -m 0644 nyancat.1 %{buildroot}/%{_mandir}/man1/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
