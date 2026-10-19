%global source0_hash 14a691c2dec509d85632fbfc2149effc41425b09196b12f1113ce89ab632a2fb
%global github_owner    os-autoinst
%global github_name     xterm_console
%global github_version  1.1
Name:           xterm-console
Version:        %{github_version}
Release:        1%{?dist}
Summary:        A Linux vt console look-alike xterm wrapper
License:        MIT
URL:            https://github.com/%{github_owner}/%{github_name}
Source0:        https://github.com/%{github_owner}/%{github_name}/archive/%{version}/%{github_name}-%{version}.tar.gz
BuildArch:      noarch
Requires:           xterm
Requires(post):     mkfontscale
Requires(postun):   mkfontscale
Supplements:    os-autoinst
# oreon:deps
BuildRequires:  bdftopcf
BuildRequires:  kbd-misc
BuildRequires:  perl-interpreter
# /oreon:deps
%description
xterm-console runs an xterm that tries to look as much as possible
like a console. It reads the current color configuration from the
kernel, and the package includes copies of the system console fonts
converted to the PCF format for xterm to use.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{github_name}-%{github_version}

%build

chmod +x ./psf2bdf.pl
for font in %{_prefix}/lib/kbd/consolefonts/*.psfu.gz; do
    fontname="${font##*/}"
    fontname="${fontname%.psfu.gz}"
    gunzip -c $font | ./psf2bdf.pl | sed -e "s,FONT \+-psf-,FONT ${fontname}," > "$fontname".bdf
done
for i in *.bdf; do
    bdftopcf "$i" | gzip -9 >"${i%.bdf}.pcf.gz"
done
%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/X11/fonts/misc/
install -m 0755 xterm-console %{buildroot}%{_bindir}
install -m 0644 *.pcf.gz %{buildroot}%{_datadir}/X11/fonts/misc/
%oreon_autofiles main

%post

mkfontdir %{_datadir}/X11/fonts/misc
%postun

if [ -d %{_datadir}/X11/fonts/misc ]; then
    mkfontdir %{_datadir}/X11/fonts/misc
fi
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
