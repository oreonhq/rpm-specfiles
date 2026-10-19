%global source0_hash 8d11fc1969ec908b996e04d2d266137fa167221152d2a9e4197308393b41bf03
Name:       imgp
Version:    3.0
Release:        1%{?dist}
Summary:        Multi-core batch image resizer and rotator
License:    GPL-3.0-only
URL:        https://github.com/jarun/imgp
Source0:        https://github.com/jarun/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:  noarch
Requires:   python3-pillow
# oreon:deps
BuildRequires:  make
# /oreon:deps
%description
imgp is a command line image resizer and rotator for JPEG and PNG images. 
It can resize (or thumbnail) and rotate thousands of images in a go,
at lightning speed, while saving significantly on storage.

Powered by multiprocessing, an intelligent adaptive algorithm, 
recursive operations, shell completion scripts, EXIF preservation (and more), 
imgp is a very flexible utility with well-documented easy to use options.

imgp intends to be a stronger replacement of the Nautilus Image Converter 
extension, not tied to any file manager and way faster. On desktop environments 
(like Xfce or LxQt) which do not integrate Nautilus, imgp will save your day.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}
sed -i '1s/env //' imgp

%build

%install
%make_install PREFIX=%{_prefix}
install -Dpm0644 -t %{buildroot}%{_datadir}/bash-completion/completions \
  auto-completion/bash/imgp-completion.bash
install -Dpm0644 -t %{buildroot}%{_datadir}/fish/vendor_functions.d \
  auto-completion/fish/imgp.fish
install -Dpm0644 -t %{buildroot}%{_datadir}/zsh/site-functions \
  auto-completion/zsh/_imgp
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
