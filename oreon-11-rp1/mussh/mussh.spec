%global source0_hash 6ba883cfaacc3f54c2643e8790556ff7b17da73c9e0d4e18346a51791fedd267

Name:           mussh
Version:        1.0
Release:        29%{?dist}
Summary:        Multihost SSH wrapper

License:        GPL-1.0-or-later
URL:            http://www.sourceforge.net/projects/mussh
Source0:        http://downloads.sourceforge.net/mussh/mussh-%{version}.tgz

BuildArch:      noarch
Requires:       openssh-clients

%description
Mussh is a shell script that allows you to execute a command or script
over ssh on multiple hosts with one command. When possible mussh will use
ssh-agent and RSA/DSA keys to minimize the need to enter your password
more than once.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n mussh

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin/
install -p mussh $RPM_BUILD_ROOT/usr/bin/
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1/
gzip mussh.1
install -p mussh.1.gz ${RPM_BUILD_ROOT}%{_mandir}/man1/

%files
%doc INSTALL README BUGS CHANGES EXAMPLES
%{_bindir}/mussh
%{_mandir}/man1/*

%changelog
%autochangelog
