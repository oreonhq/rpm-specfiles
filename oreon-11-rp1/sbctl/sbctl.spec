%global source0_hash d274451b145b0aaecfdf2d01ad45473b61ab40f3f58e4735cee50aa7573c584d

# https://gitlab.archlinux.org/archlinux/packaging/packages/sbctl/-/blob/main/PKGBUILD?ref_type=heads
%global fingerprint C100346676634E80C940FB9E9C02FF419FECBE16

Name:           sbctl
Version:        0.18
Release:        1%{?dist}
Summary:        Secure Boot key manager

License:        MIT
URL:            https://github.com/Foxboron/sbctl
Source0:        https://github.com/Foxboron/sbctl/releases/download/%{version}/sbctl-%{version}.tar.gz
Source1:        https://github.com/Foxboron/sbctl/releases/download/%{version}/sbctl-%{version}.tar.gz.sig
Source2:        https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x%{fingerprint}#/%{fingerprint}.gpg

ExclusiveArch:  %{golang_arches}

Requires:       binutils
Requires:       util-linux

Recommends:     systemd-udev

BuildRequires:  asciidoc
BuildRequires:  git
BuildRequires:  go-rpm-macros
BuildRequires:  gpgverify
BuildRequires:  pkgconfig(libpcsclite)

%description
sbctl intends to be a user-friendly secure boot key manager capable of setting
up secure boot, offer key management capabilities, and keep track of files that
needs to be signed in the boot chain.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

sed -i.orig '/go build/d' Makefile
! diff -q Makefile.orig Makefile

sed -i.orig '/libpcsclite_real\.so\.1/ s,/usr/lib,%{_libdir},' lsm/lsm.go
! diff -q lsm/lsm.go.orig lsm/lsm.go


%build
export GOPATH=%{_builddir}/go
%global gomodulesmode GO111MODULE=on
%gobuild -o sbctl ./cmd/sbctl
%make_build


%install
%make_install PREFIX=%{_prefix}

# Debian only.
rm %{buildroot}%{_prefix}/lib/kernel/postinst.d/91-sbctl.install


%transfiletriggerin -P 1 -- /boot /efi /usr/lib /usr/libexec
if [[ ! -f /run/ostree-booted ]] && grep -q -m 1 -e '\.efi$' -e '/vmlinuz$'; then
    exec </dev/null
    %{_bindir}/sbctl sign-all -g
fi


%files
%license LICENSE
%doc README.md
%ghost %dir %{_sysconfdir}/sbctl
%ghost %config(noreplace) %{_sysconfdir}/sbctl/sbctl.conf
%{_bindir}/sbctl
%{_prefix}/lib/kernel/install.d/91-sbctl.install
%{_mandir}/man5/sbctl.conf.5*
%{_mandir}/man8/sbctl.8*
%{_datadir}/bash-completion/completions/sbctl
%{_datadir}/fish/vendor_completions.d/sbctl.fish
%{_datadir}/zsh/site-functions/_sbctl


%changelog
%autochangelog