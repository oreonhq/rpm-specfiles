%global cionly 0

%global _fontname google-noto
%global fontname %{_fontname}
%global fontconf %{_fontname}
%global common_desc Noto fonts aims to remove tofu from web by providing fonts for all \
Unicode supported scripts. Its design goal is to achieve visual harmonization\
between multiple scripts. Noto family supports almost all scripts available\
in Unicode.\
%{nil}

%global srcver	2026.04.01
%global majorver	%{lua: v, _ = string.gsub(rpm.expand("%{srcver}"), "(%d+)%.%d+%.%d+", "%1"); print(v)}
%global minorver	%{lua: v, _ = string.gsub(rpm.expand("%{srcver}"), "%d+%.(%d+)%.%d+", "%1"); print(v)}
%global patchver	%{lua: v, _ = string.gsub(rpm.expand("%{srcver}"), "%d+%.%d+%.(%d+)", "%1"); print(v)}
%global rpmver	%{lua: print(string.format("%04d%02d%02d", tonumber(rpm.expand("%{majorver}")), tonumber(rpm.expand("%{minorver}")), tonumber(rpm.expand("%{patchver}"))))}
# for default font
%global hprio	56
# for default font but static
%global	shprio	57
# for non-default
%global mprio	58
# for non-default and rarely used font
%global lprio	62
# for non-latin and default
%global	nlat_hprio	65-0
# for non-latin and default but static
%global	nlat_shprio	65-2
# for non-latin and non-default
%global	nlat_mprio	66
# for non-latin and non-default and rarely used font
%global	nlat_lprio	67

Name:           %{fontname}-fonts
Version:        %{rpmver}
Release:        30%{?dist}
Summary:        Hinted and Non Hinted OpenType fonts for Unicode scripts
License:        OFL-1.1
URL:            https://notofonts.github.io/
Source0:        https://github.com/notofonts/notofonts.github.io/archive/refs/tags/noto-monthly-release-%{srcver}.zip
Source1:        google-noto-sans-math-vf.conf
Source2:        google-noto-sans-math.conf
Source3:        google-noto-naskh-arabic-ex.conf
Source4:        google-noto-znamenny-musical-notation.conf
Source8:	google-noto-sans-sinhala-ex.conf
Source9:	google-noto-fonts.gen.lua

BuildArch:      noarch
BuildRequires:  fonts-rpm-macros
Requires:       fontpackages-filesystem

%description
%common_desc


%package common
Summary:        Common files for Noto fonts

%description common
Common files for Google Noto fonts.

%{lua:
local function slurp(p)
  local f = io.open(p, "r")
  if not f then return nil end
  local s = f:read("*a")
  f:close()
  return s
end
local base = "google-noto-fonts.gen.lua"
local sd = string.gsub(rpm.expand("%{_sourcedir}"), "/+$", "")
local sp = string.gsub(rpm.expand("%{_specdir}"), "/+$", "")
local paths = {
  base,
  "./" .. base,
  sd .. "/" .. base,
  sp .. "/" .. base,
}
local body = nil
for i = 1, #paths do
  body = slurp(paths[i])
  if body then break end
end
if not body then
  error("google-noto-fonts.gen.lua: run spectool from the dir that contains it, or install it under SOURCES or SPECS (Source9)")
end
assert(load(body))()
}

%prep
%setup -q -c -n noto-fonts-%{srcver}
# Split colon macros to one name per line under %%{_builddir}. Do not use %%{_specdir} for this:
# parse-time Lua and %%prep/%%install can disagree on where the spec lives on ORBS workers.
printf '%s' '%{noto_fcconflist}' | tr ':' '\n' > "%{_builddir}/noto-fcconf-install.list"
printf '%s' '%{noto_metafilelist}' | tr ':' '\n' > "%{_builddir}/noto-metainfo-install.list"


%build
%if %{cionly}
exit 1
%endif
%{notobuild_fcconf}


%install
install -m 0755 -d %{buildroot}%{_fontbasedir}/google-noto
for f in */fonts/*/unhinted/ttf/Noto*.ttf */fonts/*/hinted/ttf/Noto*.ttf; do
  install -m 0644 -p $f %{buildroot}%{_fontbasedir}/google-noto/
done
install -m 0755 -d %{buildroot}%{_fontbasedir}/google-noto-vf
install -m 0644 -p */fonts/*/unhinted/slim-variable-ttf/Noto*.ttf %{buildroot}%{_fontbasedir}/google-noto-vf/

# remove display fonts. this isn't shipped in upstream anymore.
# use find not bare globs so missing names do not make rm complain
find %{buildroot}%{_fontbasedir}/google-noto %{buildroot}%{_fontbasedir}/google-noto-vf -maxdepth 1 \( \
  -name 'NotoSansDisplay*.ttf' -o -name 'NotoSans-Display*.ttf' -o -name 'NotoSerifDisplay*.ttf' \) \
  -exec rm -f {} + 2>/dev/null || :
find %{buildroot}%{_fontbasedir}/google-noto %{buildroot}%{_fontbasedir}/google-noto-vf -maxdepth 1 \
  \( -name 'Noto*Test-*.ttf' -o -name 'Noto*Test*.ttf' \) -exec rm -f {} + 2>/dev/null || :
# Noto Sans Phags Pa has been renamed to Noto Sans PhagsPa but shipped in the archive somehow
#   https://github.com/notofonts/phags-pa/commit/b85e2b0a38ad21d0196104e791e0b15bafedaf66
find %{buildroot}%{_fontbasedir}/google-noto -maxdepth 1 -name 'NotoSansPhags-Pa*.ttf' -exec rm -f {} + 2>/dev/null || :

# fc-scan in script expects fonts are already installed
bash "%{_specdir}/debug-noto-metainfo-build.sh"
%{notobuild_filelist}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir} \
                   %{buildroot}%{_metainfodir}

# bash -x plus megabyte-long colon lists blow log parsers. Names are one per line in %%{_builddir} (see %%prep).
set +x
while IFS= read -r f || [[ -n "${f}" ]]; do
    [[ -z "${f}" ]] && continue
    install -m 0644 -p "${f}" "%{buildroot}%{_fontconfig_templatedir}/${f}"
    ln -s "$(realpath --relative-to="%{buildroot}%{_fontconfig_confdir}" "%{buildroot}%{_fontconfig_templatedir}/${f}")" \
	  "%{buildroot}%{_fontconfig_confdir}/${f}"
done < "%{_builddir}/noto-fcconf-install.list"
while IFS= read -r f || [[ -n "${f}" ]]; do
    [[ -z "${f}" ]] && continue
    install -m 0644 -p "${f}" "%{buildroot}%{_metainfodir}/${f}"
done < "%{_builddir}/noto-metainfo-install.list"
set -x

%check
set +x
while IFS= read -r f || [[ -n "${f}" ]]; do
    [[ -z "${f}" ]] && continue
    xmllint --loaddtd --valid --nonet "%{buildroot}%{_fontconfig_templatedir}/${f}"
done < "%{_builddir}/noto-fcconf-install.list"
while IFS= read -r f || [[ -n "${f}" ]]; do
    [[ -z "${f}" ]] && continue
    appstream-util validate-relax --nonet "%{buildroot}%{_metainfodir}/${f}" || (cat "%{buildroot}%{_metainfodir}/${f}"; exit 1)
done < "%{_builddir}/noto-metainfo-install.list"
set -x

%files common
%license */LICENSE
%doc */README.md


%changelog
* Tue Apr 21 2026 Brandon Lester <blester@oreonhq.com> - 20260401-29
- %%prep: write noto-fcconf-install.list and noto-metainfo-install.list under %%{_builddir} (printf plus tr). %%install/%%check read those paths so ORBS does not depend on parse-time files next to the spec in %%{_specdir}

* Tue Apr 21 2026 Brandon Lester <blester@oreonhq.com> - 20260401-28
- gen.lua: write noto-fcconf-install.list and noto-metainfo-install.list (one name per line) for %%install/%%check so huge colon lists never hit bash argv limits or bash -x log truncation

* Mon Apr 20 2026 Brandon Lester <blester@oreonhq.com> - 20260401-20
- gen.lua: define notobuild_filelist macro (%%install used it but it was never defined, leaving literal %{notobuild_filelist} in shell and causing "fg: no job control")

* Mon Apr 20 2026 Brandon Lester <blester@oreonhq.com> - 20260401-19
- gen.lua metainfo: print command-substitution output with printf (do not execute XML lines as shell commands), fixes debug-noto-metainfo-build.sh "<font>Noto: command not found" and "<languages>: command not found"

* Mon Apr 20 2026 Brandon Lester <blester@oreonhq.com> - 20260401-18
- gen.lua metainfo: static packages use find -name PREFIX*.ttf (not only hyphenated -regex) so NotoSans.ttf matches, always echo a fallback <font>Noto FAMILY</font>, printf newline after fc-scan (fixes ORBS google-noto-sans-fonts "No family names provided")

* Mon Apr 20 2026 Brandon Lester <blester@oreonhq.com> - 20260401-17
- gen.lua metainfo: use fc-scan format \\n instead of a real newline inside -f so Fedora 43 mock emits <provides> (fixes ORBS %%install "No family names provided")

* Mon Apr 20 2026 Brandon Lester <blester@oreonhq.com> - 20260401-16
- Load gen.lua from cwd, %%{_sourcedir}, or %%{_specdir} (rpmbuild %%{_specdir} is SPECS not the git tree, so spectool from the package dir must find Source9 by basename)

* Mon Apr 20 2026 Brandon Lester <blester@oreonhq.com> - 20260401-15
- Move large embedded %%{lua:…} body to Source9 google-noto-fonts.gen.lua and load with dofile (rpmspec fails on megabyte inline lua with "unclosed macro or bad line continuation")
- Metainfo debug script: expanded buildroot path and fc-scan %% escapes kept in gen.lua

* Mon Apr 20 2026 Brandon Lester <blester@oreonhq.com> - 20260401-14
- Lua metainfo root path: build %%{RPM_BUILD_ROOT} fallback with string.char(36) so rpmspec does not treat $ as macro syntax (fixes "unclosed macro" parse error)

* Mon Apr 20 2026 Brandon Lester <blester@oreonhq.com> - 20260401-13
- Metainfo shell in debug script: bake expanded %%{buildroot} via Lua or RPM_BUILD_ROOT fallback (literal %%{buildroot} in that file is never expanded by bash)

* Mon Apr 20 2026 Brandon Lester <blester@oreonhq.com> - 20260401-12
- Lua: write debug-noto-*-build.sh under %%{_specdir}, not cwd (fixes mock %%install "No such file" for metainfo script)

* Mon Apr 20 2026 Brandon Lester <blester@oreonhq.com> - 20260401-11
- Fix %%install path to generated metainfo script by invoking it from %%{_specdir}
- Resolve "bash: ./debug-noto-metainfo-build.sh: No such file or directory" on ORBS

* Mon Apr 20 2026 Brandon Lester <blester@oreonhq.com> - 20260401-10
- Run generated metainfo script file directly in %%install so XML files are created exactly as emitted by Lua
- Avoid macro re-expansion mangling of the multiline metainfo command block

* Mon Apr 20 2026 Brandon Lester <blester@oreonhq.com> - 20260401-9
- Fix metainfo generation redirection so org.fedoraproject.*.metainfo.xml files are actually created before install
- Keep command substitutions inside a single heredoc write path and escape $PDX literal in XML header

* Mon Apr 20 2026 Brandon Lester <blester@oreonhq.com> - 20260401-8
- Fix fcconf and metainfo loops to actually split colon lists in bash (%%install and %%check use read -a)
- Avoid install "File name too long" from treating the whole %{noto_fcconflist} macro as one filename

* Mon Apr 20 2026 Brandon Lester <blester@oreonhq.com> - 20260401-7
- %%install/%%check: stop bash -x from reprinting the entire fcconf list every loop (set +x, set -- + IFS=:)
- fontconfig symlinks: realpath relative to dirs under %%{buildroot}, not host /etc and /usr

* Mon Apr 20 2026 Brandon Lester <blester@oreonhq.com> - 20260401-6
- Metainfo: quoted heredoc for static XML then run fc-scan $(…) outside it (bash no longer sees nested quotes in one cat)

* Mon Apr 20 2026 Brandon Lester <blester@oreonhq.com> - 20260401-5
- Metainfo: embed release date from Lua not $(date …) in heredoc, use string.char(39) for shell quotes (fixes bash EOF in matching quote)
- AppStream fc-scan wrappers stay single-quoted via Q concat

* Mon Apr 20 2026 Brandon Lester <blester@oreonhq.com> - 20260401-4
- Fix rpmspec Lua parse error from printf single-quote escaping, use echo plus printf %%s for AppStream blocks

* Mon Apr 20 2026 Brandon Lester <blester@oreonhq.com> - 20260401-3
- AppStream lang lines: real newline in fc-scan -f (\\n became stray n after </lang>), wrap with printf %%s per line
- Remove optional fonts with find -exec so empty globs do not rm error

* Mon Apr 20 2026 Brandon Lester <blester@oreonhq.com> - 20260401-2
- Generate AppStream provides and languages from fc-scan without nested echo sh (stops multi-megabyte install script lines and huge build logs)

* Sun Apr 19 2026 Brandon Lester <blester@oreonhq.com> - 20260401-1
- import
