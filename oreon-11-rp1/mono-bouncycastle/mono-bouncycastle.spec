%global source0_hash 4cc2e885ab9c84cd1345e1f3a6f34fe75e988d9b38d95fdd7849fdc5be81b12c

%global debug_package %{nil}

Name:           mono-bouncycastle
Version:        1.8.10
Release:        12%{?dist}
Summary:        Bouncy Castle Crypto Package for Mono

# Files in crypto/bzip2/ are ASL 2.0 licensed,
# everything else is MIT.
# Automatically converted from old format: MIT and ASL 2.0 - review is highly recommended.
License:        LicenseRef-Callaway-MIT AND Apache-2.0
URL:            http://www.bouncycastle.org/csharp/
Source0:        https://github.com/bcgit/bc-csharp/archive/release-%{version}.tar.gz

BuildRequires:  mono-devel, nant, log4net
BuildRequires:  unzip

# Mono only available on these:
ExclusiveArch: %mono_arches
# nant is not available on armv7hl, see
# https://bugzilla.redhat.com/show_bug.cgi?id=1923663
ExcludeArch:    armv7hl

%description
The Bouncy Castle Crypto package is a C# implementation of cryptographic
algorithms. It is a port of the Bouncy Castle Java APIs, with
approximately 80% of the functionality ported. The C# API is constantly
kept up to date with bug fixes and new test cases from the Java build
(and vice versa sometimes), thus benefiting from the large user base
and real-world use the Java version has seen.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n bc-csharp-release-%{version}
sed -i 's/set-mono-4.0-framework-props/set-mono-4.5-framework-props/g' crypto/NBuild.build

%build
# Use the mono system key instead of generating our own here.
cp -a /etc/pki/mono/mono.snk BouncyCastle.snk
pushd crypto/
nant -D:use-strong-name=true compile-release
popd

%install
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/mono/gac/
gacutil -i crypto/api/bin/release/BouncyCastle.Crypto.dll -f -package bouncycastle -root $RPM_BUILD_ROOT%{_prefix}/lib

%files
%license crypto/License.html
%doc crypto/Contributors.html
%doc crypto/Readme.html
%{_prefix}/lib/mono/gac/*/
%{_prefix}/lib/mono/bouncycastle/

%changelog
%autochangelog
