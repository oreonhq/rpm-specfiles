%global source0_hash 8fd13eaaa266f7ee91f85c1ea97c86d9c9cc985969db9059cdebcb1e1b7bdbe6

Name:		pbzip2
Version:	1.1.13
Release:	16%{?dist}
Summary:	Parallel implementation of bzip2
URL:		https://launchpad.net/pbzip2
License:	bzip2-1.0.6
BuildRequires: make
BuildRequires:	gcc-c++
BuildRequires:	bzip2-devel
Source0:	https://launchpad.net/pbzip2/1.1/%{version}/+download/pbzip2-%{version}.tar.gz
Patch0:		%{name}-1.1.12-buildflags.patch

%description
PBZIP2 is a parallel implementation of the bzip2 block-sorting file
compressor that uses pthreads and achieves near-linear speedup on SMP
machines.  The output of this version is fully compatible with bzip2
v1.0.2 or newer (ie: anything compressed with pbzip2 can be 
decompressed with bzip2).


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1
f=AUTHORS; iconv -f iso-8859-1 -t utf-8 $f > $f.utf8 && mv $f.utf8 $f


%build
%set_build_flags
%make_build


%install
install -D -m755 %{name} %{buildroot}%{_bindir}/%{name}
install -D -m644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
ln -sf ./%{name} %{buildroot}%{_bindir}/pbunzip2
ln -sf ./%{name} %{buildroot}%{_bindir}/pbzcat



%files
%doc AUTHORS ChangeLog README
%license COPYING
%{_bindir}/%{name}
%{_bindir}/pbunzip2
%{_bindir}/pbzcat
%{_mandir}/man1/*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.13-16
- Prepare for Oreon 11 (RP1)
