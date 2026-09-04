%global source0_hash ad2186c976c588c483bfd6a7166fba2e2ec743027e14be4618ba1f0e5baadab9

Version:        1.7.0
Release:        1%{?dist}
URL:            https://vercel.com/font

%global foundry vercel
%global fontlicense OFL-1.1
%global fontlicenses geist-font-%{version}/OFL.txt
%global fontdocsex %{fontlicenses}

%global sans_description %{expand:Geist is a sans-serif typeface designed for
legibility and simplicity. It is a modern, geometric typeface that is based on
the principles of classic Swiss typography. It is designed to be used in
headlines, logos, posters, and other large display sizes.}

%global mono_description %{expand:Geist Mono is a monospaced typeface that has
been crafted to be the perfect partner to Geist Sans. It is designed to be used
in code editors, diagrams, terminals, and other text-based interfaces where code
is represented.}

%global fontfamily0 Geist
%global fontsummary0 The Geist font family
%global fonts0 geist-font-%{version}/fonts/Geist/otf/*.otf
%global fontconfs0 %{SOURCE10}
%global fontdescription0 %{expand:%{sans_description}

This package contains the Geist font family.}

%global fontfamily1 Geist VF
%global fontsummary1 The Geist font family (variable)
%global fonts1 geist-font-%{version}/fonts/Geist/variable/*.ttf
%global fontconfs1 %{SOURCE11}
%global fontdescription1 %{expand:%{sans_description}

This package contains the variable Geist font family.}

%global fontfamily2 Geist Mono
%global fontsummary2 The Geist Mono font family
%global fonts2 geist-font-%{version}/fonts/GeistMono/otf/*.otf
%global fontconfs2 %{SOURCE12}
%global fontdescription2 %{expand:%{mono_description}

This package contains the Geist Mono font family.}

%global fontfamily3 Geist Mono VF
%global fontsummary3 The Geist Mono font family (variable)
%global fonts3 geist-font-%{version}/fonts/GeistMono/variable/*.ttf
%global fontconfs3 %{SOURCE13}
%global fontdescription3 %{expand:%{mono_description}

This package contains the variable Geist Mono font family.}

Source0:        https://github.com/vercel/geist-font/releases/download/%{version}/geist-font-%{version}.zip
Source10:       63-vercel-geist.conf
Source11:       63-vercel-geist-vf.conf
Source12:       63-vercel-geist-mono.conf
Source13:       63-vercel-geist-mono-vf.conf

%fontpkg -a

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c

%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a
%fontfiles -a

%changelog
%autochangelog
