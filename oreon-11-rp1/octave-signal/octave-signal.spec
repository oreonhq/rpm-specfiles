%global source0_hash 6a8b4b8cf0b3019d984fde75af947ae73e9a1c509890552cd5e113f7ba89038c
%global octpkg signal
Name:           octave-%{octpkg}
Version:        1.4.7
Release:        1%{?dist}
Summary:        Signal processing tools for Octave
License:        GPL-3.0-or-later
URL:            http://octave.sourceforge.net/signal/
Source0:        https://github.com/gnu-octave/%{name}/releases/download/%{version}/%{octpkg}-%{version}.tar.gz
ExcludeArch:    s390x
ExcludeArch:    aarch64
Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave
Requires:       octave-control >= 2.4.5
# oreon:deps
BuildRequires:  octave-control
BuildRequires:  octave-devel
# /oreon:deps
%description
Signal processing tools, including filtering, windowing and display

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{octpkg}-%{version}
for i in inst/*.m; do
  iconv -f iso8859-1 -t utf-8 $i > $i.conv && mv -f $i.conv $i
done;

%build

%octave_pkg_build
%install
%octave_pkg_install
%oreon_autofiles main

%check

%octave_pkg_check
%post

%octave_cmd pkg rebuild
%preun

%octave_pkg_preun
%postun

%octave_cmd pkg rebuild
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
