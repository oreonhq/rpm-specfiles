%global source0_hash cc8596af3325ecb18ebd6ec2baee550e82cb7b2da19588f3f843b02e943a15a9

Name:           bam
Version:        0.5.1

Release:        20%{?dist}
Summary:        A build-system

License:        zlib
URL:            http://matricks.github.com/bam/
Source0:        https://github.com/matricks/bam/archive/v%{version}.tar.gz

BuildRequires:  gcc

%description
A tool that controls process of producing executables of
software from its source code. Used to build the Teeworlds game.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
sh -x make_unix.sh %{optflags}

%install
install -D -p -m 0755 %{name} \
        %{buildroot}%{_bindir}/%{name}

%files
%doc docs/ examples/
%{_bindir}/%{name}

%changelog
%autochangelog
