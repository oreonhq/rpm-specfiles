%global provider        github
%global provider_tld    com
%global project sgallagher
%global repo sscg
# https://github.com/sgallagher/sscg
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}

%{!?meson_test: %global meson_test %{__meson} test -C %{_vpath_builddir} --num-processes %{_smp_build_ncpus} --print-errorlogs}

Name:           sscg
Version:        4.0.3
Release:        %autorelease
Summary:        Simple Signed Certificate Generator

License:        GPL-3.0-or-later WITH cryptsetup-OpenSSL-exception
URL:            https://%{provider_prefix}
Source0:        https://github.com/sgallagher/sscg/archive/refs/tags/sscg-4.0.3.tar.gz
BuildRequires:  gcc
BuildRequires:  libtalloc-devel
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  popt-devel
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  help2man

# Upstream patch to avoid segfaults when receiving bad CLI arguments
# https://github.com/sgallagher/sscg/commit/0c37e7ace585cfb550a0ffd9d5c331d059fd687f
Patch: 0001-Avoid-segfault-on-receiving-bad-CLI-arguments.patch
# oreon url source checksums begin
%global source0_sha256 277e994b50dea28bfec64b43ba689a4fb5c31bb777c7aedacbdb1f491dd48c60
%global source0_file sscg-4.0.3.tar.gz
# oreon url source checksums end


%description
A utility to aid in the creation of more secure "self-signed"
certificates. The certificates created by this tool are generated in a
way so as to create a CA certificate that can be safely imported into a
client machine to trust the service certificate without needing to set
up a full PKI environment and without exposing the machine to a risk of
false signatures from the service certificate.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/sscg-4.0.3.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "277e994b50dea28bfec64b43ba689a4fb5c31bb777c7aedacbdb1f491dd48c60" || { echo "oreon: Source0 SHA256 mismatch for sscg-4.0.3.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -n sscg-sscg-%{version}


%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test -t 10

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.0.3-1
- Prepare for Oreon 11 (RP1)
