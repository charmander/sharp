{
  'targets': [{
    'target_name': 'sharp',
    'variables': {
      # Build the PKG_CONFIG_PATH environment variable with all possible combinations
      'pkg_config_path': '<!(which brew >/dev/null 2>&1 && eval $(brew --env) && echo $PKG_CONFIG_LIBDIR || true):$PKG_CONFIG_PATH:/usr/local/lib/pkgconfig:/usr/lib/pkgconfig',
    },
    'sources': [
      'src/common.cc',
      'src/metadata.cc',
      'src/operations.cc',
      'src/pipeline.cc',
      'src/sharp.cc',
      'src/utilities.cc',
    ],
    'include_dirs': [
      '<!(node -e "require(\'nan\')")',
      '<!@(PKG_CONFIG_PATH="<(pkg_config_path)" pkg-config --cflags-only-I vips-cpp vips glib-2.0 | sed s\/-I//g)',
    ],
    'libraries': [
      '<!@(PKG_CONFIG_PATH="<(pkg_config_path)" pkg-config --libs vips-cpp)',
    ],
    'cflags_cc': [
      '-std=c++14',
      '-fexceptions',
      '-Wall',
      '-O3'
    ],
  }],
}
