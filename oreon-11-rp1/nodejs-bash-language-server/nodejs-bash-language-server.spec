%global source0_hash b6067cb1444a699a5ab145ad2f27e0451f7b35d6c8617142097a758094e49b83
%{?nodejs_default_filter}
%define pkg_name bash-language-server
Name:           nodejs-bash-language-server
Version:        5.8.0
Release:        1%{?dist}
Summary:        A language server for Bash
License:        MIT
Url:            https://github.com/bash-lsp/bash-language-server
Source0:        https://github.com/bash-lsp/%{pkg_name}/archive/server-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        %{pkg_name}-%{version}-vendor.tar.zst
Source2:        bash-language-server-bundled-licenses.txt
BuildArch:      noarch
ExclusiveArch: %{nodejs_arches} noarch
Recommends:     ShellCheck
# oreon:deps
BuildRequires:  fdupes
BuildRequires:  nodejs
BuildRequires:  nodejs-npm
BuildRequires:  nodejs-packaging
BuildRequires:  npm
BuildRequires:  npm(typescript)
BuildRequires:  perl-interpreter
BuildRequires:  pnpm
# /oreon:deps
%description
Bash language server implementation based on Tree Sitter and its grammar for
Bash with explainshell integration.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pkg_name}-server-%{version} -a1 -p1

cp %{SOURCE2} .

%build

pnpm install --offline --frozen-lockfile --store-dir="$(pwd)/.pnpm-store"
npm run compile
%install
rm -rf node_modules/
pnpm install --production --offline --frozen-lockfile --package-import-method copy --store-dir="$(pwd)/.pnpm-store"
for S in $(grep -l '#!.*node' \
    server/out/cli.js \
    server/node_modules/ajv/scripts/* \
    server/node_modules/escodegen/bin/* \
    server/node_modules/esprima/bin/* \
    server/node_modules/performance-now/test/scripts/* \
    server/node_modules/pn/scripts/* \
    server/node_modules/sshpk/bin/* \
    server/node_modules/uuid/bin/* \
    server/node_modules/vscode-languageserver/bin/* \
    ) ; do
    SB="${S}.backup"
    cp ${S} ${SB}
    perl -p -i -e 's|#!/usr/bin/env node|#!%{_bindir}/node|g' $S
    diff -urN ${SB} ${S} || :
    rm ${SB}
done
install -d -m 0755 %{buildroot}%{nodejs_sitelib}/%{pkg_name}/
cp -av server %{buildroot}%{nodejs_sitelib}/%{pkg_name}/
cp -av node_modules %{buildroot}%{nodejs_sitelib}/%{pkg_name}/
install -d -m 0755 %{buildroot}%{_bindir}
cat << EOF > %{buildroot}%{_bindir}/%{pkg_name}
export NODE_ENV=production
exec /usr/bin/node %{nodejs_sitelib}/%{pkg_name}/server/out/cli.js "\$@"
EOF
chmod +x %{buildroot}%{_bindir}/%{pkg_name}
find %{buildroot}%{nodejs_sitelib}/%{pkg_name} -name "*.bak" -delete
find %{buildroot}%{nodejs_sitelib}/%{pkg_name} -type f -name "\.*" -delete
find %{buildroot}%{nodejs_sitelib}/%{pkg_name} -type d -name "\.bin" -print0 | xargs -0 rm -rf
find %{buildroot}%{nodejs_sitelib}/%{pkg_name} -type d -name "\.github" -print0 | xargs -0 rm -rf
rm -rf %{buildroot}%{nodejs_sitelib}/%{pkg_name}/server/node_modules/ajv/scripts/
rm -rf %{buildroot}%{nodejs_sitelib}/%{pkg_name}/server/node_modules/dashdash/etc/
rm -rf %{buildroot}%{nodejs_sitelib}/%{pkg_name}/server/node_modules/performance-now/test/
rm %{buildroot}%{nodejs_sitelib}/%{pkg_name}/server/src/get-options.sh
rm %{buildroot}%{nodejs_sitelib}/%{pkg_name}/server/node_modules/@types/fuzzy-search
rm %{buildroot}%{nodejs_sitelib}/%{pkg_name}/server/node_modules/@types/node-fetch
rm %{buildroot}%{nodejs_sitelib}/%{pkg_name}/server/node_modules/@types/turndown
rm %{buildroot}%{nodejs_sitelib}/%{pkg_name}/server/node_modules/@types/urijs
%fdupes %{buildroot}%{nodejs_sitelib}/%{pkg_name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
