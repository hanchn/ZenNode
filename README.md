## 🧠 一、代码级优化方向

1. [**避免同步阻塞代码**（如 `fs.readFileSync`、`crypto.pbkdf2Sync`）](./files/avoid-sync-blocking.md)
2. [**合理使用 async/await、Promise.all、并发控制**](./files/async-await-promise.md)
3. [**使用流（Stream）处理大文件，避免一次性加载进内存**](./files/stream-large-file.md)
4. [**避免使用 JSON.parse(JSON.stringify(obj)) 深拷贝大对象**](./files/avoid-json-deepcopy.md)
5. [**缓存频繁计算或访问的数据（如 LRU 缓存）**](./files/cache-frequent-data.md)
6. [**使用原生方法替代第三方库（如用 `Buffer.from()` 替代 `lodash.cloneDeep`）**](./files/native-vs-thirdparty.md)
7. [**限制闭包滥用，减少内存泄漏风险**](./files/closure-memory-leak.md)
8. [**使用 V8 优化技巧，如避免稀疏数组、使用隐藏类优化对象结构**](./files/v8-optimization.md)

---

## 🛠️ 二、运行时优化方向

9. [**合理设置 Node.js 的 `--max-old-space-size` 参数**](./files/max-old-space-size.md)
10. [**使用 `worker_threads` 多线程处理计算密集任务**](./files/worker-threads.md)
11. [**使用 `Cluster` 模块进行多进程扩展**](./files/cluster-multi-process.md)
12. [**避免垃圾回收频繁触发（观察 GC 日志与内存占用）**](./files/gc-optimize.md)
13. [**启用 Node.js Profiler (`--inspect`, `--prof`) 分析性能瓶颈**](./files/node-profiler.md)

---

## 🌐 三、网络与请求优化方向

14. [**使用 HTTP keep-alive 复用连接**](./files/http-keep-alive.md)
15. [**压缩 HTTP 响应（gzip/brotli）**](./files/http-compress.md)
16. [**合理设置缓存头（Cache-Control、ETag）**](./files/http-cache-header.md)
17. [**使用 CDN 缓存静态资源**](./files/cdn-static.md)
18. [**避免 N+1 请求，批量处理 API 请求**](./files/avoid-n-plus-1.md)
19. [**防止请求体过大（设置 `body-parser` 限制）**](./files/body-parser-limit.md)

---

## ⚙️ 四、中间件和框架优化方向

20. [**移除无用中间件，精简中间件链**](./files/remove-unused-middleware.md)
21. [**基于路由分组进行中间件注入（避免全局处理）**](./files/route-group-middleware.md)
22. [**优化 Express/Koa 路由匹配（避免正则太复杂）**](./files/route-regexp-optimize.md)
23. [**使用轻量化框架代替如 Fastify 替代 Express（更快）**](./files/fastify-vs-express.md)

---

## 🧩 五、数据库性能优化

24. [**使用连接池（如 `mysql2`, `pg-pool`）**](./files/db-connection-pool.md)
25. [**为常用查询建立索引**](./files/db-index.md)
26. [**使用 Redis/Memcached 做缓存降压**](./files/db-cache.md)
27. [**避免数据库 N+1 查询，优化 SQL**](./files/db-n-plus-1.md)
28. [**采用分页、流式查询处理大量数据**](./files/db-pagination-stream.md)

---

## 📦 六、打包与部署优化

29. [**代码分模块拆包，避免单体臃肿**](./files/code-split.md)
30. [**启用 AOT（如 esbuild）提前编译代码**](./files/aot-esbuild.md)
31. [**使用 PM2/forever 管理进程，支持负载均衡**](./files/pm2-forever.md)
32. [**Docker 镜像瘦身，避免多层冗余**](./files/docker-slim.md)

---

## 🔍 七、监控与可视化

33. [**接入性能监控工具：Prometheus + Grafana**](./files/prometheus-grafana.md)
34. [**引入 APM 工具（如 NewRelic、Skywalking、Jaeger）**](./files/apm-tools.md)
35. [**日志记录耗时与堆栈（如 pino、winston）**](./files/log-time-stack.md)
36. [**使用 flamegraph 分析 CPU 密集函数**](./files/flamegraph.md)

---

## 🧪 八、测试与压测方向

37. [**编写性能基准测试（如使用 autocannon, Artillery）**](./files/benchmark-test.md)
38. [**设置错误熔断机制（如 `opossum`）**](./files/circuit-breaker.md)
39. [**构建压测环境，模拟高并发/突发请求**](./files/stress-test-env.md)
40. [**分析性能报告，定位瓶颈模块并持续优化**](./files/performance-report.md)

