%global source0_hash f487c39d2913f371eb42dab078559a902da69acca38a9ebec7640a6581535ba3
Name:       mathjax
Version:    4.1.3
Release:        1%{?dist}
Summary:        JavaScript library to render math in the browser
License:    Apache-2.0
URL:        http://mathjax.org
Source0:        https://github.com/mathjax/MathJax/archive/%{version}.tar.gz#/mathjax-%{version}.tar.gz
BuildArch:  noarch
Requires:        web-assets-filesystem
# oreon:deps
BuildRequires:  web-assets-devel
# /oreon:deps
%description
MathJax is an open-source JavaScript display engine for LaTeX, MathML,
and AsciiMath notation that works in all modern browsers. It requires no
setup on the part of the user (no plugins to download or software to
install), so the page author can write web documents that include
mathematics and be confident that users will be able to view it
naturally and easily. Supports LaTeX, MathML, and AsciiMath notation
in HTML pages.

%prep

%setup -q -n MathJax-%{version}
find . -name .htaccess -print -delete

%build

%install
mkdir -p %{buildroot}%{_jsdir}/mathjax
cp -pr a11y/ adaptors/ input/ output/ sre/ ui/ \
    core.js loader.js startup.js require.mjs \
    node-main.cjs node-main.js node-main.mjs node-main-setup.cjs \
    tex-chtml.js tex-chtml-nofont.js tex-mml-chtml.js tex-mml-chtml-nofont.js \
    tex-mml-svg.js tex-mml-svg-nofont.js tex-svg.js tex-svg-nofont.js \
    mml-chtml.js mml-chtml-nofont.js mml-svg.js mml-svg-nofont.js \
    %{buildroot}%{_jsdir}/mathjax/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
