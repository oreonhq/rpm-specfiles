%global source0_hash a0779c45179a846986a852bce31bddbe9259b594574f75c0ec146d0567058f7e
%bcond_without tests
Name:           yt-dlp
Version:        2026.08.19
Release:        1%{?dist}
Summary:        A command-line program to download videos from online video platforms
License:        Unlicense
URL:            https://github.com/yt-dlp/yt-dlp
Source0:        https://github.com/%{name}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch:          17491.patch
Patch:          0002-Restore-compatibility-with-pytest-9.patch
BuildArch:      noarch
%if %{with tests}
%endif
Requires:       yt-dlp+default = %{?epoch:%{epoch}:}%{version}-%{release}
Recommends:     /usr/bin/ffmpeg
Recommends:     /usr/bin/ffprobe
Suggests:       python3dist(keyring)
Provides:       yt-dlp-bash-completion = %{version}-%{release}
Obsoletes:      yt-dlp-bash-completion < 2025.09.26-2
Provides:       yt-dlp-fish-completion = %{version}-%{release}
Obsoletes:      yt-dlp-fish-completion < 2025.09.26-2
Provides:       yt-dlp-zsh-completion = %{version}-%{release}
Obsoletes:      yt-dlp-zsh-completion < 2025.09.26-2
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.27.0
Requires:       python3-yt-dlp = %{version}-%{release}
# /oreon:deps
%package -n       python3-yt-dlp+default
Summary:        Metapackage for python3-yt-dlp default extras
Requires:       python3-yt-dlp = %{version}-%{release}
Requires:       python3dist(requests) >= 2.32.2
Requires:       python3dist(requests) < 3
Requires:       python3dist(urllib3) >= 2.0.2
Requires:       python3dist(urllib3) < 3
Requires:       python3dist(websockets) >= 13.0
Requires:       python3dist(yt-dlp-ejs) == 0.8.0
Provides:       python3dist(yt-dlp[default]) = %{version}-%{release}

%description -n python3-yt-dlp+default
Metapackage for python3-yt-dlp default extras.

%package -n       python3-yt-dlp+curl-cffi
Summary:        Metapackage for python3-yt-dlp curl-cffi extras
Requires:       python3-yt-dlp = %{version}-%{release}
Requires:       python3dist(curl-cffi) >= 0.5.10
Requires:       python3dist(curl-cffi) < 0.17
Provides:       python3dist(yt-dlp[curl-cffi]) = %{version}-%{release}

%description -n python3-yt-dlp+curl-cffi
Metapackage for python3-yt-dlp curl-cffi extras.

%package -n       python3-yt-dlp+secretstorage
Summary:        Metapackage for python3-yt-dlp secretstorage extras
Requires:       python3-yt-dlp = %{version}-%{release}
Provides:       python3dist(yt-dlp[secretstorage]) = %{version}-%{release}

%description -n python3-yt-dlp+secretstorage
Metapackage for python3-yt-dlp secretstorage extras.

%package -n       python3-yt-dlp+deno
Summary:        Metapackage for python3-yt-dlp deno extras
Requires:       python3-yt-dlp = %{version}-%{release}
Requires:       python3dist(deno) >= 2.6.6
Provides:       python3dist(yt-dlp[deno]) = %{version}-%{release}

%description -n python3-yt-dlp+deno
Metapackage for python3-yt-dlp deno extras.

%package -n       python3-yt-dlp+pin
Summary:        Metapackage for python3-yt-dlp pin extras
Requires:       python3-yt-dlp = %{version}-%{release}
Requires:       python3dist(brotli) == 1.2.0
Requires:       python3dist(brotlicffi) == 1.2.0.1
Requires:       python3dist(certifi) == 2026.7.22
Requires:       python3dist(charset-normalizer) == 3.5.0
Requires:       python3dist(idna) == 3.18
Requires:       python3dist(mutagen) == 1.48.1
Requires:       python3dist(pycryptodomex) == 3.23.0
Requires:       python3dist(requests) == 2.34.2
Requires:       python3dist(urllib3) == 2.7.0
Requires:       python3dist(websockets) == 16.1.1
Requires:       python3dist(websockets) == 17.0.1
Requires:       python3dist(yt-dlp-ejs) == 0.8.0
Provides:       python3dist(yt-dlp[pin]) = %{version}-%{release}

%description -n python3-yt-dlp+pin
Metapackage for python3-yt-dlp pin extras.

%package -n       python3-yt-dlp+pin-curl-cffi
Summary:        Metapackage for python3-yt-dlp pin-curl-cffi extras
Requires:       python3-yt-dlp = %{version}-%{release}
Requires:       python3dist(certifi) == 2026.7.22
Requires:       python3dist(cffi) == 2.1.1
Requires:       python3dist(curl-cffi) == 0.16.0
Requires:       python3dist(pycparser) == 3.0
Requires:       python3dist(typing-extensions) == 4.16.0
Provides:       python3dist(yt-dlp[pin-curl-cffi]) = %{version}-%{release}

%description -n python3-yt-dlp+pin-curl-cffi
Metapackage for python3-yt-dlp pin-curl-cffi extras.

%package -n       python3-yt-dlp+pin-secretstorage
Summary:        Metapackage for python3-yt-dlp pin-secretstorage extras
Requires:       python3-yt-dlp = %{version}-%{release}
Requires:       python3dist(cffi) == 2.1.1
Requires:       python3dist(cryptography) == 50.0.0
Requires:       python3dist(jeepney) == 0.9.0
Requires:       python3dist(pycparser) == 3.0
Requires:       python3dist(secretstorage) == 3.5.0
Requires:       python3dist(typing-extensions) == 4.16.0
Provides:       python3dist(yt-dlp[pin-secretstorage]) = %{version}-%{release}

%description -n python3-yt-dlp+pin-secretstorage
Metapackage for python3-yt-dlp pin-secretstorage extras.

%package -n       python3-yt-dlp+pin-deno
Summary:        Metapackage for python3-yt-dlp pin-deno extras
Requires:       python3-yt-dlp = %{version}-%{release}
Requires:       python3dist(deno) == 2.9.5
Provides:       python3dist(yt-dlp[pin-deno]) = %{version}-%{release}

%description -n python3-yt-dlp+pin-deno
Metapackage for python3-yt-dlp pin-deno extras.

%description
yt-dlp is a command-line program to download videos from many different online
video platforms, such as youtube.com. The project is a fork of youtube-dl with
additional features and fixes.

%prep

%autosetup -p1

# TODO: Figure out https://bugzilla.redhat.com/show_bug.cgi?id=2405578
# Users can configure JS challenges manually for now.
tomcli set pyproject.toml arrays delitem \
    project.optional-dependencies.default 'yt-dlp-ejs.*'

# Remove -s from shebang so users can install extra deps or plugins (or yt-dlp-ejs) using pip.
%undefine _py3_shebang_s

# Remove unnecessary shebangs
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +

%build

make yt-dlp.1 completion-bash completion-zsh completion-fish
%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main

%check

%if %{with tests}
%pytest -k "not download and not test_verify_cert[Websockets]"
%endif
%files

%changelog

%autochangelog
