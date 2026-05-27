%global source0_hash none

Name:           desktop-backgrounds
Version:        11
Release:        1%{?dist}
Summary:        Default desktop background compatibility symlinks

License:        MIT
URL:            https://oreonhq.com
BuildArch:      noarch

Requires:       oreon-backgrounds
Provides:       desktop-backgrounds-compat = %{version}-%{release}
Obsoletes:      desktop-backgrounds-compat < %{version}-%{release}

%description
Compatibility package that ensures %{_datadir}/backgrounds/default.png and
%{_datadir}/backgrounds/default.jxl exist for consumers such as SDDM and Plasma.
It selects an available image from %{_datadir}/backgrounds and updates symlinks.

%post
set -e
bg_dir="%{_datadir}/backgrounds"
mkdir -p "$bg_dir"

pick_background() {
    for candidate in "$bg_dir"/*.png "$bg_dir"/*.jxl "$bg_dir"/*.jpg "$bg_dir"/*.jpeg "$bg_dir"/*.webp; do
        [ -e "$candidate" ] || continue
        case "$(basename "$candidate")" in
            default.png|default.jxl)
                continue
                ;;
        esac
        echo "$candidate"
        return 0
    done
    return 1
}

chosen="$(pick_background || true)"
if [ -n "$chosen" ]; then
    ln -sfn "$(basename "$chosen")" "$bg_dir/default.png"
    ln -sfn "$(basename "$chosen")" "$bg_dir/default.jxl"
fi

%posttrans
set -e
bg_dir="%{_datadir}/backgrounds"

if [ ! -e "$bg_dir/default.png" ] || [ ! -e "$bg_dir/default.jxl" ]; then
    for candidate in "$bg_dir"/*.png "$bg_dir"/*.jxl "$bg_dir"/*.jpg "$bg_dir"/*.jpeg "$bg_dir"/*.webp; do
        [ -e "$candidate" ] || continue
        case "$(basename "$candidate")" in
            default.png|default.jxl)
                continue
                ;;
        esac
        ln -sfn "$(basename "$candidate")" "$bg_dir/default.png"
        ln -sfn "$(basename "$candidate")" "$bg_dir/default.jxl"
        break
    done
fi

%postun
if [ "$1" -eq 0 ]; then
    rm -f "%{_datadir}/backgrounds/default.png" "%{_datadir}/backgrounds/default.jxl"
fi

%files
%ghost %{_datadir}/backgrounds/default.png
%ghost %{_datadir}/backgrounds/default.jxl

%changelog
* Tue Apr 14 2026 Oreon Packaging Team <packaging@oreonhq.com> - 11-1
- Add desktop-backgrounds compatibility package and provide desktop-backgrounds-compat
- Manage %{_datadir}/backgrounds/default.{png,jxl} symlinks for desktop consumers
