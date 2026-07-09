%global source0_hash 9a966c1340a1a1d92073091643687b1205c46b57017c5da2bf7e97e3f5729a5a

%global goipath github.com/rfjakob/gocryptfs/v2

Summary:        Encrypted overlay filesystem written in Go
Name:           gocryptfs
Version:        2.6.1
Release:        2%{?dist}
License:        MIT
URL:            https://nuetzlich.net/gocryptfs/
Source0:        https://github.com/rfjakob/gocryptfs/releases/download/v%{version}/gocryptfs_v%{version}_src-deps.tar.gz

BuildRequires:  golang
BuildRequires:  fuse3-devel
BuildRequires:  openssl-devel

Requires:       fuse3

%description
gocryptfs is an encrypted overlay filesystem written in Go. It is FUSE
based, has a good balance between speed, security and reliability, and
supports offline decryption of the file names in addition to the contents.

Backs the encrypted-vault-on-demand feature of plasma-vault.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}_v%{version}_src-deps

%build
export GOFLAGS="-mod=vendor"
export GO111MODULE=on
go build -buildmode=pie -ldflags "-X main.GitVersion=%{version} -X main.BuildDate=$(date -u +%%Y-%%m-%%d)" -o gocryptfs .
go build -buildmode=pie -o gocryptfs-xray/gocryptfs-xray ./gocryptfs-xray

%install
install -D -p -m 0755 gocryptfs %{buildroot}%{_bindir}/gocryptfs
install -D -p -m 0755 gocryptfs-xray/gocryptfs-xray %{buildroot}%{_bindir}/gocryptfs-xray

%files
%license LICENSE
%doc README.md Documentation/MANPAGE.md Documentation/MANPAGE-XRAY.md
%{_bindir}/gocryptfs
%{_bindir}/gocryptfs-xray

%changelog
%autochangelog
