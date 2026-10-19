%global source0_hash 606e286125f98bd2eeacbe566992e51ded3ba32cb4f9f746ce0a09eab97a3050
Name:           eg
Version:        1.7.5.2
Release:        1%{?dist}
Summary:        Git for mere mortals
License:        GPL-2.0-only
URL:            http://www.gnome.org/~newren/eg/
Source0:        %{name}-%{version}.tar.gz
Patch0:		eg-1.7.5.2-fix-use-false-detection.patch
Requires:       perl-interpreter
BuildArch:      noarch
Requires:       git
# oreon:deps
BuildRequires:  bash-completion
BuildRequires:  perl-generators
# /oreon:deps
%description
Easy Git (eg) is a wrapper for git, designed to make git easy to learn and use.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .false

# Filter unwanted Requires:
cat << \EOF > %{name}-prov
#!/bin/sh
%{__perl_requires} $* |\
  sed -e '/perl(the)/d;/perl(an)/d;/perl(it)/d;/perl(one)/d'
EOF

%define __perl_requires %{_builddir}/%{name}-%{version}/%{name}-prov
chmod +x %{__perl_requires}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}/
install -m 755 eg $RPM_BUILD_ROOT/%{_bindir}/
bashcompdir=$(pkg-config --variable=completionsdir bash-completion || :)
if [ "$bashcompdir" ]; then
    install -Dpm 644 bash-completion-eg.sh $RPM_BUILD_ROOT$bashcompdir/eg
    echo %{_datadir}/bash-completion > %{name}.files
else
    install -Dpm 644 bash-completion-eg.sh \
        $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/eg
    echo %{_sysconfdir}/bash_completion.d > %{name}.files
fi
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
