%global source0_hash 3b1dd1596fe5404b690b4bc3ff06627a6f87f484607b6516f38a443d527bb794

%global buildver 217
%global patchlvl 21

Name:           trilead-ssh2
Version:        %{buildver}.%{patchlvl}
Release:        19%{?dist}
Summary:        SSH-2 protocol implementation in pure Java

# Project is under BSD, but some parts are MIT licensed
# see LICENSE.txt for more information
# One file is ISC licensed: The bundled implementation of BCrypt.java
# One file is RSA licensed: src/com/trilead/ssh2/crypto/digest/MD5.java
# Automatically converted from old format: BSD and MIT and ISC and RSA - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT AND ISC AND LicenseRef-RSA

# Jenkins fork is used because the original sources of this library,
# "ganymed" and then "trilead" are both defunct and the original
# project sites are unavailable. However Jenkins project continues
# to maintain it
URL:            https://github.com/jenkinsci/trilead-ssh2
Source0:        https://github.com/jenkinsci/trilead-ssh2/archive/%{name}-build-%{buildver}-jenkins-%{patchlvl}.tar.gz

# Source of bundled BCrypt implementation, taken from:
# https://mvnrepository.com/artifact/org.connectbot.jbcrypt/jbcrypt/1.0.0
Source1:  BCrypt.java
Provides: bundled(jbcrypt) = 1.0.0

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(net.i2p.crypto:eddsa)

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

%description
Trilead SSH-2 for Java is a library which implements the SSH-2 protocol in pure
Java (tested on J2SE 1.4.2 and 5.0). It allows one to connect to SSH servers
from within Java programs. It supports SSH sessions (remote command execution
and shell access), local and remote port forwarding, local stream forwarding,
X11 forwarding and SCP. There are no dependencies on any JCE provider, as all
crypto functionality is included.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{name}-build-%{buildver}-jenkins-%{patchlvl}

# jbcrypt is not available in Fedora, it is bundled instead
mkdir -p src/org/mindrot/jbcrypt
cp -p %{SOURCE1} src/org/mindrot/jbcrypt
%pom_remove_dep "org.connectbot.jbcrypt:jbcrypt"

# test dependency not available in Fedora
%pom_remove_dep "org.testcontainers:testcontainers"

# compat symlink/alias
%mvn_file  : %{name}/%{name} %{name}
%mvn_alias : "org.tmatesoft.svnkit:trilead-ssh2" "com.trilead:trilead-ssh2"

%build
# Skip tests due to unavailability of test deps
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt
%doc HISTORY.txt README.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
%autochangelog
